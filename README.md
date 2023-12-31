# flowbite-icons-mithril

500+ SVG [Flowbite icons](https://flowbite.com/icons/) components for [Mithril](https://mithril.js.org/).

## Installation
```shell
npm i -D flowbite-icons-mithril
```

## Usage
```javascript
import m from "mithril";
import { BugIcon } from "flowbite-icons-mithril/solid";

export const MyComponent = {
  view: () => m(BugIcon),
};
```

## Attributes
### Size
The following size helpers are available: Default: `sm`.

| Size | CSS Classes |
|------|-------------|
| xs   | w-3 h-3     |
| sm	 | w-4 h-4     |
| md	 | w-5 h-5     |
| lg	 | w-6 h-6     |
| xl	 | w-8 h-8     |

Using:
```javascript
m(BugIcon, {size: "lg"})
```

### Class
You can override the default sizes and pass any [Tailwind CSS](https://flowbite.com/tools/tailwind-cheat-sheet/) classes like this:
```javascript
m(BugIcon, {class: "h-24 w-24 text-blue-700 mr-4"})
```

### Attributes
You can pass any extra attributes you want in the normal Mithril way:
```javascript
m(BugIcon, {"aria-hidden": true})
```
