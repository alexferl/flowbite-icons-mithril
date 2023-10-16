# flowbite-icons-mithril

## Getting started
```shell
npm i flowbite-icons-mithril
```

### Example
```javascript
import m from "mithril";
import { BugIcon } from "flowbite-icons-mithril/solid"

export const MyComponent = () => ({
  view: () => {
    return m(BugIcon, {size: "md", class: "any flowbite classes you want to add"})
  }
});
```

The following size helpers are available:
```javascript
xs: "w-3 h-3"
sm: "w-4 h-4"
md: "w-5 h-5" // default
lg: "w-6 h-6"
xl: "w-8 h-8"
```
