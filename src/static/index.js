// The Monaco Editor can be easily created, given an
// empty container and an options literal.
// Two members of the literal are "value" and "language".
// The editor takes the full size of its container.

editor = monaco.editor.create(document.getElementById("container"), {
  value:
    'from typing import *\n\ndef life(\n    f: Callable[str, Generator[int, str, bool]],\n    g: Awaitable[Sequence[int]]\n) -> Dict[List[Set[FrozenSet[int]]], str]:\n    return {[{frozenset(42)}]: "Hello World!"}\n\nfromkeys: Callable[List[int], Dict[int, List[Union[Segment, None]]]]',
  language: "python",
  wordWrap: "on",
  fontSize: 18,

  renderLineHighlight: false,
  fontLigatures: "'cv01', 'cv02', 'cv04', 'ss05', 'ss03', 'cv30'",
  fontFamily: "Fira Code,Cascadia Code,Menlo,Monaco,Consolas,Courier New",
  fontWeight: 500,
  renderWhitespace: "all",

  minimap: {
    scale: 2,
  },

  cursorBlinking: "expand",
  cursorSmoothCaretAnimation: true,
  smoothScrolling: true,

  padding: { top: "5px" },
});

fetch("./static/themes/Copilot.json")
  .then((data) => data.json())
  .then((data) => {
    monaco.editor.defineTheme("copilot", data);
    monaco.editor.setTheme("copilot");
  });

action_button = document.getElementById("typesplain");
form = document.getElementById("typesplain-form");
action_button.addEventListener("click", (e) => {
  e.preventDefault();

  if (document.getElementById("code") === null) {
    const hiddenCodeInput = document.createElement("input");
    hiddenCodeInput.type = "hidden";
    hiddenCodeInput.id = "code";
    hiddenCodeInput.name = "code";
    hiddenCodeInput.value = editor.getValue().replaceAll("\n", ";");
    form.appendChild(hiddenCodeInput);
  } else {
    const hiddenCodeInput = document.getElementById("code");
    hiddenCodeInput.value = editor.getValue().replaceAll("\n", ";");
  }
  form.submit();
  return false;
});
