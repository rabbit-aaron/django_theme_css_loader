{
  const currentScript = document.currentScript;
  const htmlEl = document.documentElement;
  const linkEl = document.createElement("link");
  linkEl.setAttribute("rel", "stylesheet");
  linkEl.setAttribute("media", currentScript.getAttribute("data-media"));
  document.head.appendChild(linkEl);

  const currentTheme = () => {
    const themeVal = htmlEl.getAttribute("data-theme");
    if (themeVal !== "auto") {
      return themeVal;
    }
    if (matchMedia('(prefers-color-scheme: dark)').matches) {
      return "dark";
    }
    return "light";
  };

  const updateTheme = () => {
    const theme = currentTheme();
    linkEl.setAttribute("href", currentScript.getAttribute(`data-${theme}-css`));
  };

  const mutationObserver = new MutationObserver(updateTheme);
  mutationObserver.observe(htmlEl, {attributeFilter: ["data-theme"]});
}
