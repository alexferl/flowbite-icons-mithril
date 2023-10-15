import glob
import shutil
from pathlib import Path
from xml.dom import minidom


def parse_svg(element, out="", last=True):
    for elem in element:
        if elem.attributes:
            classes = "{"
            if elem.nodeName == "svg":
                classes += '"class": className,'
            for k, v in elem.attributes.items():
                classes += f'"{k}": "{v}",'
            classes += "}"
            out += f'm("{elem.nodeName}",{classes}'
            if not last:
                out += "),"
            else:
                out += ","

        if elem.hasChildNodes:
            elem_child_nodes = [x for x in elem.childNodes if x.nodeName != "#text"]
            for child in elem_child_nodes:
                if child.attributes:
                    d = {k: v for k, v in child.attributes.items()}
                    out += f'm("{child.nodeName}",{d},'
                if child.hasChildNodes:
                    child_nodes = [x for x in child.childNodes if x.nodeName != "#text"]
                    if len(child_nodes) > 1:
                        out += "["
                    if child.lastChild:
                        return parse_svg(child_nodes, out, True)
                    else:
                        return parse_svg(child_nodes, out, False)
                if child.lastChild:
                    out += "]"
            else:
                out += "),"

    if "[" in out:
        out += "]"
    out += "))"
    out.replace("'", '"')
    return out


def process_files():
    # cleanup folder first
    out_path = "dist"
    if Path(out_path).is_dir():
        shutil.rmtree(out_path)

    root_dir = "flowbite-icons/src"
    outline_dir = f"{root_dir}/outline/"
    solid_dir = f"{root_dir}/solid/"

    for dir in [outline_dir, solid_dir]:
        files = list(glob.iglob(dir + "**/*.svg", recursive=True))
        files_len = len(files) - 1
        imports = []
        for idx, filename in enumerate(sorted(files)):
            split = filename.split("/")
            package = split[-3]

            name = "".join(
                x for x in split[-1].split(".svg")[0].title() if not x.isspace()
            ).replace("-", "")
            name += "Icon"
            doc = minidom.parse(filename)
            svg = doc.getElementsByTagName("svg")
            out = parse_svg(svg)

            template = f"""import m from "mithril";
import {{ twMerge }} from "tailwind-merge";

export const {name} = () => ({{
  view: ({{ attrs }}) => {{
    const sizes = {{
      xs: "w-3 h-3",
      sm: "w-4 h-4",
      md: "w-5 h-5",
      lg: "w-6 h-6",
      xl: "w-8 h-8"
    }};
    const size = attrs.size || "md"
    const className = twMerge("shrink-0", sizes[size], attrs.class)

    return {out}
  }}
}});
        """

            p = Path(f"{out_path}/{package}")
            p.mkdir(exist_ok=True, parents=True)

            with open(p / f"{name}.js", "w") as dest:
                dest.write(template)

            imports.append(f'export {{ {name} }} from "./{name}.js";\n')

            if idx == files_len:
                with open(p / "index.js", "a") as f:
                    f.write("".join(sorted(imports)))


if __name__ == "__main__":
    process_files()
