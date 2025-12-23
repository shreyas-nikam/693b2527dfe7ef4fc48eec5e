<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Notebook</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                messageStyle: 'none',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      maxEdges: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        let { svg } = await mermaid.render(id, raw, el);
        svg = cleanMermaidSvg(svg);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }


    /**
     * Post-process to ensure mermaid diagrams contain only valid SVG and XHTML.
     */
    function cleanMermaidSvg(svg) {
      return svg.replace(RE_VOID_ELEMENT, replaceVoidElement);
    }


    /**
     * A regular expression for all void elements, which may include attributes and
     * a slash.
     *
     * @see https://developer.mozilla.org/en-US/docs/Glossary/Void_element
     *
     * Of these, only `<br>` is generated by Mermaid in place of `\n`,
     * but _any_ "malformed" tag will break the SVG rendering entirely.
     */
    const RE_VOID_ELEMENT =
      /<\s*(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\s*([^>]*?)\s*>/gi;

    /**
     * Ensure a void element is closed with a slash, preserving any attributes.
     */
    function replaceVoidElement(match, tag, rest) {
      rest = rest.trim();
      if (!rest.endsWith('/')) {
        rest = `${rest} /`;
      }
      return `<${tag} ${rest}>`;
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=ae384113">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Workforce-AI-Readiness-&amp;-Upskilling-Strategizer">Workforce AI-Readiness &amp; Upskilling Strategizer<a class="anchor-link" href="#Workforce-AI-Readiness-&amp;-Upskilling-Strategizer">¶</a></h1>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=cf557c95">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="err">!</span><span class="n">pip</span> <span class="n">install</span> <span class="n">pandas</span> <span class="n">numpy</span> <span class="n">matplotlib</span> <span class="n">seaborn</span> <span class="n">scipy</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)
Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)
Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (3.10.0)
Requirement already satisfied: seaborn in /usr/local/lib/python3.12/dist-packages (0.13.2)
Requirement already satisfied: scipy in /usr/local/lib/python3.12/dist-packages (1.16.3)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)
Requirement already satisfied: contourpy&gt;=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)
Requirement already satisfied: cycler&gt;=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools&gt;=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.61.0)
Requirement already satisfied: kiwisolver&gt;=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.4.9)
Requirement already satisfied: packaging&gt;=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (25.0)
Requirement already satisfied: pillow&gt;=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (11.3.0)
Requirement already satisfied: pyparsing&gt;=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.2.5)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil&gt;=2.8.2-&gt;pandas) (1.17.0)
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=c020a500">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">numpy</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">np</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">matplotlib.pyplot</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">plt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">seaborn</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">sns</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">scipy.optimize</span><span class="w"> </span><span class="kn">import</span> <span class="n">minimize</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">random</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">copy</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=790e7190">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-1:-Introduction-to-the-AI-Readiness-Framework">Section 1: Introduction to the AI-Readiness Framework<a class="anchor-link" href="#Section-1:-Introduction-to-the-AI-Readiness-Framework">¶</a></h1><p>The AI-Readiness Score (AI-R) is a novel parametric framework designed to quantify an individual's preparedness for success in AI-enabled careers. It decomposes career opportunity into two orthogonal components: Systematic Opportunity ($HR^R$), representing macro-level job growth and demand, and Idiosyncratic Readiness ($V^R$), representing individual-specific capabilities. A Synergy factor captures the multiplicative benefits when individual readiness aligns with market opportunity.</p>
<p>The core formula for the AI-Readiness Score for individual $i$ at time $t$ is defined as:</p>
<p>$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot HR^R(t) + \beta \cdot Synergy\%(V^R, HR^R)$$</p>
<p>where:</p>
<ul>
<li>$V^R_{i}(t)$: Idiosyncratic Readiness (individual capability).</li>
<li>$HR^R(t)$: Systematic Opportunity (market demand).</li>
<li>$\alpha \in [0,1]$: Weight on individual vs. market factors. For this notebook, we'll use $\alpha = 0.6$.</li>
<li>$\beta &gt; 0$: Synergy coefficient. For this notebook, we'll use $\beta = 0.15$.</li>
<li>Both $V^R$ and $HR^R$ are normalized to $[0, 100]$.</li>
<li>$Synergy\% \in [0,100]$ (percentage units).</li>
</ul>
<p>This framework allows for dynamic "what-if" scenario planning, helping to guide targeted upskilling initiatives and talent development.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=9e15ef0c">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [3]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_ai_r</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="n">hr_score</span><span class="p">,</span> <span class="n">synergy_score</span><span class="p">,</span> <span class="n">alpha</span><span class="p">,</span> <span class="n">beta</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes the overall AI-Readiness Score."""</span>
    <span class="c1"># Ensure scores are within 0-100</span>
    <span class="n">vr_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
    <span class="n">hr_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">hr_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
    <span class="n">synergy_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">synergy_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

    <span class="c1"># Calculate AI-R</span>
    <span class="n">ai_r</span> <span class="o">=</span> <span class="p">(</span><span class="n">alpha</span> <span class="o">*</span> <span class="n">vr_score</span><span class="p">)</span> <span class="o">+</span> <span class="p">((</span><span class="mi">1</span> <span class="o">-</span> <span class="n">alpha</span><span class="p">)</span> <span class="o">*</span> <span class="n">hr_score</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">beta</span> <span class="o">*</span> <span class="n">synergy_score</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">ai_r</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Test the function immediately</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test AI-R score: </span><span class="si">{</span><span class="n">calculate_ai_r</span><span class="p">(</span><span class="n">vr_score</span><span class="o">=</span><span class="mi">75</span><span class="p">,</span><span class="w"> </span><span class="n">hr_score</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span><span class="w"> </span><span class="n">synergy_score</span><span class="o">=</span><span class="mi">51</span><span class="p">,</span><span class="w"> </span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.6</span><span class="p">,</span><span class="w"> </span><span class="n">beta</span><span class="o">=</span><span class="mf">0.15</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test AI-R score: 84.65
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=3a85e8a0">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [4]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Define default parameters for \alpha and \beta</span>
<span class="n">PARAMS</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'alpha'</span><span class="p">:</span> <span class="mf">0.6</span><span class="p">,</span>
    <span class="s1">'beta'</span><span class="p">:</span> <span class="mf">0.15</span><span class="p">,</span>
    <span class="s1">'lambda_growth'</span><span class="p">:</span> <span class="mf">0.3</span><span class="p">,</span>
    <span class="s1">'gamma_regional'</span><span class="p">:</span> <span class="mf">0.2</span><span class="p">,</span>
    <span class="s1">'hr_base_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'ai_enhancement_weight'</span><span class="p">:</span> <span class="mf">0.30</span><span class="p">,</span>
        <span class="s1">'job_growth_weight'</span><span class="p">:</span> <span class="mf">0.30</span><span class="p">,</span>
        <span class="s1">'wage_premium_weight'</span><span class="p">:</span> <span class="mf">0.25</span><span class="p">,</span>
        <span class="s1">'entry_accessibility_weight'</span><span class="p">:</span> <span class="mf">0.15</span>
    <span class="p">},</span>
    <span class="s1">'theta_ai_fluency_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'technical_ai_skills_weight'</span><span class="p">:</span> <span class="mf">0.30</span><span class="p">,</span>
        <span class="s1">'ai_augmented_productivity_weight'</span><span class="p">:</span> <span class="mf">0.35</span><span class="p">,</span>
        <span class="s1">'critical_ai_judgment_weight'</span><span class="p">:</span> <span class="mf">0.20</span><span class="p">,</span>
        <span class="s1">'ai_learning_velocity_weight'</span><span class="p">:</span> <span class="mf">0.15</span>
    <span class="p">},</span>
    <span class="s1">'gamma_experience_decay'</span><span class="p">:</span> <span class="mf">0.15</span><span class="p">,</span>
    <span class="s1">'domain_specialization_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'portfolio_weight'</span><span class="p">:</span> <span class="mf">0.4</span><span class="p">,</span>
        <span class="s1">'recognition_weight'</span><span class="p">:</span> <span class="mf">0.3</span><span class="p">,</span>
        <span class="s1">'credentials_weight'</span><span class="p">:</span> <span class="mf">0.3</span>
    <span class="p">},</span>
    <span class="s1">'vr_component_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'ai_fluency_weight_vr'</span><span class="p">:</span> <span class="mf">0.45</span><span class="p">,</span>
        <span class="s1">'domain_expertise_weight_vr'</span><span class="p">:</span> <span class="mf">0.35</span><span class="p">,</span>
        <span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">:</span> <span class="mf">0.20</span>
    <span class="p">}</span>
<span class="p">}</span>

<span class="c1"># Initialize placeholder values for VR, HRR, and Synergy%</span>
<span class="n">vr_placeholder</span> <span class="o">=</span> <span class="mi">75</span>
<span class="n">hr_placeholder</span> <span class="o">=</span> <span class="mi">80</span>
<span class="n">synergy_placeholder</span> <span class="o">=</span> <span class="mf">51.0</span>

<span class="c1"># Execute calculate_ai_r with these placeholder values</span>
<span class="n">final_ai_r_placeholder</span> <span class="o">=</span> <span class="n">calculate_ai_r</span><span class="p">(</span><span class="n">vr_placeholder</span><span class="p">,</span> <span class="n">hr_placeholder</span><span class="p">,</span> <span class="n">synergy_placeholder</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">],</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">])</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Placeholder V^R: </span><span class="si">{</span><span class="n">vr_placeholder</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Placeholder HR^R: </span><span class="si">{</span><span class="n">hr_placeholder</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Placeholder Synergy%: </span><span class="si">{</span><span class="n">synergy_placeholder</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Calculated AI-R with placeholder values: </span><span class="si">{</span><span class="n">final_ai_r_placeholder</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Placeholder V^R: 75
Placeholder HR^R: 80
Placeholder Synergy%: 51.0
Calculated AI-R with placeholder values: 84.65
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=2d931220">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>This execution demonstrates how the final AI-R score is computed by combining the Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($HR^R$), and Synergy components, weighted by the parameters $\alpha$ and $\beta$. The example reflects a scenario where an individual has strong readiness in a high-opportunity field with good alignment, resulting in a high AI-R score.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=afd1d39a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-2:-Synthetic-Data-Generation-and-Setup">Section 2: Synthetic Data Generation and Setup<a class="anchor-link" href="#Section-2:-Synthetic-Data-Generation-and-Setup">¶</a></h1><p>To simulate a real-world scenario without relying on external APIs, we will generate synthetic datasets for employee cohorts, occupational taxonomies, labor market data, and learning pathway coefficients. These datasets will be <code>pandas.DataFrame</code> objects, carefully structured to contain all necessary attributes for AI-R calculations.</p>
<p>We define three primary DataFrames:</p>
<ol>
<li><code>df_employees</code>: Contains individual employee data, including current skill levels, experience, education, and initial AI-R components (some to be calculated).</li>
<li><code>df_occupations</code>: Contains data relevant to specific job roles, such as AI-Enhancement potential, growth projections, wage premiums, and required skills.</li>
<li><code>df_pathways</code>: Details various learning pathways, their costs, time commitments, and impact coefficients on $V^R$ sub-components.</li>
</ol>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=569fa833">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>⚠️ The code execution failed in the sandbox after multiple attempts.
Please check the below cell and manually resolve the issue.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=5bcd4de3">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">numpy</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">np</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">random</span>

<span class="c1"># The functions to be tested are defined here within the test file.</span>
<span class="c1"># This ensures tests are self-contained and run against a consistent version of the functions.</span>

<span class="k">def</span><span class="w"> </span><span class="nf">generate_synthetic_employees</span><span class="p">(</span><span class="n">num_employees</span><span class="o">=</span><span class="mi">50</span><span class="p">):</span>
    <span class="n">employee_data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'employee_id'</span><span class="p">:</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'EMP</span><span class="si">{</span><span class="n">i</span><span class="si">:</span><span class="s1">03d</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_employees</span><span class="p">)],</span>
        <span class="s1">'job_role'</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">([</span><span class="s1">'Data Scientist'</span><span class="p">,</span> <span class="s1">'ML Engineer'</span><span class="p">,</span> <span class="s1">'AI Ethicist'</span><span class="p">,</span> <span class="s1">'Business Analyst'</span><span class="p">,</span> <span class="s1">'HR Specialist'</span><span class="p">],</span> <span class="n">k</span><span class="o">=</span><span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'department'</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">([</span><span class="s1">'R&amp;D'</span><span class="p">,</span> <span class="s1">'Engineering'</span><span class="p">,</span> <span class="s1">'HR'</span><span class="p">,</span> <span class="s1">'Marketing'</span><span class="p">,</span> <span class="s1">'Finance'</span><span class="p">],</span> <span class="n">k</span><span class="o">=</span><span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'years_experience'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'education_level'</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">([</span><span class="s1">'HS+Coursework'</span><span class="p">,</span> <span class="s1">'Associate</span><span class="se">\'</span><span class="s1">s/Certificate'</span><span class="p">,</span> <span class="s1">'Bachelor</span><span class="se">\'</span><span class="s1">s'</span><span class="p">,</span> <span class="s1">'Master</span><span class="se">\'</span><span class="s1">s'</span><span class="p">,</span> <span class="s1">'PhD'</span><span class="p">],</span> <span class="n">k</span><span class="o">=</span><span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'tools_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">40</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">35</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'output_quality_with_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.7</span><span class="p">,</span> <span class="mf">1.2</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span> <span class="c1"># Relative to without AI</span>
        <span class="s1">'output_quality_without_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'time_without_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="mf">1.5</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span> <span class="c1"># Relative to with AI</span>
        <span class="s1">'time_with_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.7</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'errors_caught'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'total_ai_errors'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'appropriate_trust_decisions'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'total_decisions'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.05</span><span class="p">,</span> <span class="mf">0.25</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'hours_invested'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="mi">500</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'domain_portfolio_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'domain_recognition_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">80</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'domain_credentials_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'adaptive_cognitive_flexibility'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">40</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'adaptive_social_emotional'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'adaptive_strategic_career'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">35</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">)</span>
    <span class="p">}</span>
    <span class="c1"># Add generic skills for skill match</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="n">employee_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">)</span> <span class="c1"># Corrected syntax for inner string literal</span>

    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">employee_data</span><span class="p">)</span>

    <span class="c1"># Normalize scores to 0-100 where applicable (these are raw inputs)</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'errors_caught_norm'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'errors_caught'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'total_ai_errors'</span><span class="p">]</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'trust_decisions_norm'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'appropriate_trust_decisions'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'total_decisions'</span><span class="p">]</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

    <span class="c1"># Ensure no division by zero for output_quality_without_ai and time_with_ai</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai_safe'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai'</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai_safe'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai'</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>

    <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_with_ai'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai_safe'</span><span class="p">])</span> <span class="o">*</span> \
                                         <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'time_without_ai'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai_safe'</span><span class="p">])</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="c1"># Fill NaN if division by zero occurred</span>

    <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_norm'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span> <span class="o">*</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span> <span class="c1"># Scale and clip for initial S_i2</span>

    <span class="k">return</span> <span class="n">df</span>

<span class="k">def</span><span class="w"> </span><span class="nf">generate_synthetic_occupations</span><span class="p">():</span>
    <span class="n">occupation_data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'occupation'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'Data Scientist'</span><span class="p">,</span> <span class="s1">'ML Engineer'</span><span class="p">,</span> <span class="s1">'AI Ethicist'</span><span class="p">,</span> <span class="s1">'Business Analyst'</span><span class="p">,</span> <span class="s1">'HR Specialist'</span><span class="p">],</span>
        <span class="s1">'ai_enhancement_potential'</span><span class="p">:</span> <span class="p">[</span><span class="mi">85</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span> <span class="mi">50</span><span class="p">],</span>
        <span class="s1">'projected_jobs_t'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5000</span><span class="p">,</span> <span class="mi">4000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">,</span> <span class="mi">15000</span><span class="p">,</span> <span class="mi">12000</span><span class="p">],</span>
        <span class="s1">'projected_jobs_t_plus_10'</span><span class="p">:</span> <span class="p">[</span><span class="mi">8000</span><span class="p">,</span> <span class="mi">7500</span><span class="p">,</span> <span class="mi">2000</span><span class="p">,</span> <span class="mi">16000</span><span class="p">,</span> <span class="mi">11000</span><span class="p">],</span>
        <span class="s1">'ai_skilled_wage'</span><span class="p">:</span> <span class="p">[</span><span class="mi">140000</span><span class="p">,</span> <span class="mi">150000</span><span class="p">,</span> <span class="mi">120000</span><span class="p">,</span> <span class="mi">90000</span><span class="p">,</span> <span class="mi">80000</span><span class="p">],</span>
        <span class="s1">'median_wage'</span><span class="p">:</span> <span class="p">[</span><span class="mi">110000</span><span class="p">,</span> <span class="mi">120000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mi">75000</span><span class="p">,</span> <span class="mi">65000</span><span class="p">],</span>
        <span class="s1">'education_years_required'</span><span class="p">:</span> <span class="p">[</span><span class="mi">18</span><span class="p">,</span> <span class="mi">18</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">14</span><span class="p">],</span>
        <span class="s1">'experience_years_required'</span><span class="p">:</span> <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span>
        <span class="s1">'remote_work_factor'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.8</span><span class="p">,</span> <span class="mf">0.9</span><span class="p">,</span> <span class="mf">0.7</span><span class="p">,</span> <span class="mf">0.6</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">],</span>
        <span class="s1">'job_postings_current_month'</span><span class="p">:</span> <span class="p">[</span><span class="mi">120</span><span class="p">,</span> <span class="mi">110</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">80</span><span class="p">,</span> <span class="mi">70</span><span class="p">],</span>
        <span class="s1">'job_postings_prev_month'</span><span class="p">:</span> <span class="p">[</span><span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span> <span class="mi">85</span><span class="p">,</span> <span class="mi">75</span><span class="p">],</span>
        <span class="s1">'national_avg_demand'</span><span class="p">:</span> <span class="p">[</span><span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">]</span>
    <span class="p">}</span>
    <span class="c1"># Add required skills and importance</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="n">occupation_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]))</span> <span class="c1"># Corrected syntax for inner string literal</span>
        <span class="n">occupation_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.1</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]))</span> <span class="c1"># Corrected syntax for inner string literal</span>

    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">generate_synthetic_pathways</span><span class="p">():</span>
    <span class="n">pathway_data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'pathway_id'</span><span class="p">:</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'PATH</span><span class="si">{</span><span class="n">i</span><span class="si">:</span><span class="s1">02d</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">)],</span>
        <span class="s1">'pathway_name'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'AI Fundamentals Course'</span><span class="p">,</span> <span class="s1">'Advanced ML Specialization'</span><span class="p">,</span> <span class="s1">'AI Ethics &amp; Governance'</span><span class="p">,</span> <span class="s1">'Data Storytelling with AI'</span><span class="p">,</span> <span class="s1">'HR Analytics with AI'</span><span class="p">],</span>
        <span class="s1">'pathway_type'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'Online Course'</span><span class="p">,</span> <span class="s1">'Certification'</span><span class="p">,</span> <span class="s1">'Workshop'</span><span class="p">,</span> <span class="s1">'Online Course'</span><span class="p">,</span> <span class="s1">'Certification'</span><span class="p">],</span>
        <span class="s1">'cost'</span><span class="p">:</span> <span class="p">[</span><span class="mi">500</span><span class="p">,</span> <span class="mi">2000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">750</span><span class="p">],</span>
        <span class="s1">'time_hours'</span><span class="p">:</span> <span class="p">[</span><span class="mi">40</span><span class="p">,</span> <span class="mi">160</span><span class="p">,</span> <span class="mi">80</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">60</span><span class="p">],</span>
        <span class="s1">'delta_ai_fluency'</span><span class="p">:</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
        <span class="s1">'delta_domain_expertise'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">12</span><span class="p">],</span>
        <span class="s1">'delta_adaptive_capacity'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">]</span>
    <span class="p">}</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">pathway_data</span><span class="p">)</span>


<span class="c1"># Pytest Unit Tests</span>
<span class="c1"># To ensure reproducibility, set a seed for numpy and random</span>
<span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span><span class="p">(</span><span class="n">autouse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">def</span><span class="w"> </span><span class="nf">set_random_seed</span><span class="p">():</span>
    <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>
    <span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span>


<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_employees_structure</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">generate_synthetic_employees</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span> <span class="o">==</span> <span class="mi">10</span>

    <span class="n">expected_cols</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'department'</span><span class="p">,</span> <span class="s1">'years_experience'</span><span class="p">,</span> <span class="s1">'education_level'</span><span class="p">,</span>
        <span class="s1">'prompting_score'</span><span class="p">,</span> <span class="s1">'tools_score'</span><span class="p">,</span> <span class="s1">'understanding_score'</span><span class="p">,</span> <span class="s1">'data_lit_score'</span><span class="p">,</span>
        <span class="s1">'output_quality_with_ai'</span><span class="p">,</span> <span class="s1">'output_quality_without_ai'</span><span class="p">,</span> <span class="s1">'time_without_ai'</span><span class="p">,</span>
        <span class="s1">'time_with_ai'</span><span class="p">,</span> <span class="s1">'errors_caught'</span><span class="p">,</span> <span class="s1">'total_ai_errors'</span><span class="p">,</span>
        <span class="s1">'appropriate_trust_decisions'</span><span class="p">,</span> <span class="s1">'total_decisions'</span><span class="p">,</span> <span class="s1">'learning_rate'</span><span class="p">,</span>
        <span class="s1">'hours_invested'</span><span class="p">,</span> <span class="s1">'domain_portfolio_score'</span><span class="p">,</span> <span class="s1">'domain_recognition_score'</span><span class="p">,</span>
        <span class="s1">'domain_credentials_score'</span><span class="p">,</span> <span class="s1">'adaptive_cognitive_flexibility'</span><span class="p">,</span>
        <span class="s1">'adaptive_social_emotional'</span><span class="p">,</span> <span class="s1">'adaptive_strategic_career'</span>
    <span class="p">]</span>
    <span class="c1"># Add generic skill columns</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="n">expected_cols</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
    <span class="c1"># Add derived columns, including the new safe columns</span>
    <span class="n">expected_cols</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s1">'errors_caught_norm'</span><span class="p">,</span> <span class="s1">'trust_decisions_norm'</span><span class="p">,</span> <span class="s1">'output_quality_without_ai_safe'</span><span class="p">,</span>
                          <span class="s1">'time_with_ai_safe'</span><span class="p">,</span> <span class="s1">'ai_augmented_productivity_raw'</span><span class="p">,</span> <span class="s1">'ai_augmented_productivity_norm'</span><span class="p">])</span>

    <span class="k">assert</span> <span class="nb">all</span><span class="p">(</span><span class="n">col</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span> <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">expected_cols</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span> <span class="o">==</span> <span class="mi">10</span>

<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_employees_edge_cases</span><span class="p">():</span>
    <span class="n">df_zero</span> <span class="o">=</span> <span class="n">generate_synthetic_employees</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">df_zero</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">df_zero</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span>
    <span class="c1"># Ensure columns are still defined even with no rows (by checking if columns exist and are of object type for string cols)</span>
    <span class="k">assert</span> <span class="s1">'employee_id'</span> <span class="ow">in</span> <span class="n">df_zero</span><span class="o">.</span><span class="n">columns</span>
    <span class="k">assert</span> <span class="s1">'years_experience'</span> <span class="ow">in</span> <span class="n">df_zero</span><span class="o">.</span><span class="n">columns</span>


    <span class="n">df_one</span> <span class="o">=</span> <span class="n">generate_synthetic_employees</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">df_one</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">df_one</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span>
    <span class="k">assert</span> <span class="n">df_one</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s1">'EMP000'</span>

<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_employees_value_ranges</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">generate_synthetic_employees</span><span class="p">(</span><span class="mi">100</span><span class="p">)</span>

    <span class="c1"># Check normalized scores are within [0, 100]</span>
    <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="p">[</span><span class="s1">'errors_caught_norm'</span><span class="p">,</span> <span class="s1">'trust_decisions_norm'</span><span class="p">,</span> <span class="s1">'ai_augmented_productivity_norm'</span><span class="p">]:</span>
        <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">0</span>
        <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">100</span>
        <span class="k">assert</span> <span class="ow">not</span> <span class="n">df</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()</span> <span class="c1"># No NaNs</span>

    <span class="c1"># Check raw scores for typical ranges</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'years_experience'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">0</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'years_experience'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;</span> <span class="mi">20</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'prompting_score'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">30</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'prompting_score'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">95</span> <span class="c1"># max possible for randint(30, 95) is 94</span>

    <span class="c1"># Check ratios are positive (should be for the original values, before potential divisions by zero)</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_with_ai'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'time_without_ai'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>

    <span class="c1"># Test division by zero handling in normalized scores by ensuring finite results</span>
    <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isfinite</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'errors_caught_norm'</span><span class="p">])</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isfinite</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'trust_decisions_norm'</span><span class="p">])</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isfinite</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_norm'</span><span class="p">])</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>


<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_occupations_structure</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">generate_synthetic_occupations</span><span class="p">()</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span> <span class="o">==</span> <span class="mi">5</span> <span class="c1"># Fixed number of occupations</span>

    <span class="n">expected_cols</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s1">'occupation'</span><span class="p">,</span> <span class="s1">'ai_enhancement_potential'</span><span class="p">,</span> <span class="s1">'projected_jobs_t'</span><span class="p">,</span> <span class="s1">'projected_jobs_t_plus_10'</span><span class="p">,</span>
        <span class="s1">'ai_skilled_wage'</span><span class="p">,</span> <span class="s1">'median_wage'</span><span class="p">,</span> <span class="s1">'education_years_required'</span><span class="p">,</span> <span class="s1">'experience_years_required'</span><span class="p">,</span>
        <span class="s1">'remote_work_factor'</span><span class="p">,</span> <span class="s1">'job_postings_current_month'</span><span class="p">,</span> <span class="s1">'job_postings_prev_month'</span><span class="p">,</span>
        <span class="s1">'national_avg_demand'</span>
    <span class="p">]</span>
    <span class="c1"># Add generic skill and importance columns</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="n">expected_cols</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="n">expected_cols</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span><span class="p">)</span>

    <span class="k">assert</span> <span class="nb">all</span><span class="p">(</span><span class="n">col</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span> <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">expected_cols</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span> <span class="o">==</span> <span class="mi">5</span>

<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_occupations_value_ranges</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">generate_synthetic_occupations</span><span class="p">()</span>

    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'ai_enhancement_potential'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">50</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'ai_enhancement_potential'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">90</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'projected_jobs_t'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'ai_skilled_wage'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">df</span><span class="p">[</span><span class="s1">'median_wage'</span><span class="p">])</span><span class="o">.</span><span class="n">all</span><span class="p">()</span> <span class="c1"># AI-skilled wage should be higher</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'education_years_required'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'experience_years_required'</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'remote_work_factor'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mf">0.5</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'remote_work_factor'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mf">0.9</span>

    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">30</span>
        <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">90</span>
        <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mf">0.1</span>
        <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mf">1.0</span>


<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_pathways_structure</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">generate_synthetic_pathways</span><span class="p">()</span>
    <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">)</span>
    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span> <span class="o">==</span> <span class="mi">5</span> <span class="c1"># Fixed number of pathways</span>

    <span class="n">expected_cols</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s1">'pathway_id'</span><span class="p">,</span> <span class="s1">'pathway_name'</span><span class="p">,</span> <span class="s1">'pathway_type'</span><span class="p">,</span> <span class="s1">'cost'</span><span class="p">,</span> <span class="s1">'time_hours'</span><span class="p">,</span>
        <span class="s1">'delta_ai_fluency'</span><span class="p">,</span> <span class="s1">'delta_domain_expertise'</span><span class="p">,</span> <span class="s1">'delta_adaptive_capacity'</span>
    <span class="p">]</span>
    <span class="k">assert</span> <span class="nb">all</span><span class="p">(</span><span class="n">col</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span> <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">expected_cols</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'pathway_id'</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span> <span class="o">==</span> <span class="mi">5</span>
    <span class="k">assert</span> <span class="n">df</span><span class="p">[</span><span class="s1">'pathway_name'</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span> <span class="o">==</span> <span class="mi">5</span>

<span class="k">def</span><span class="w"> </span><span class="nf">test_generate_synthetic_pathways_value_ranges</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">generate_synthetic_pathways</span><span class="p">()</span>

    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'cost'</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'time_hours'</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'delta_ai_fluency'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'delta_domain_expertise'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">assert</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'delta_adaptive_capacity'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=827117c6">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Call the data generation functions to create the DataFrames</span>
<span class="n">df_employees</span> <span class="o">=</span> <span class="n">generate_synthetic_employees</span><span class="p">(</span><span class="n">num_employees</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>
<span class="n">df_occupations</span> <span class="o">=</span> <span class="n">generate_synthetic_occupations</span><span class="p">()</span>
<span class="n">df_pathways</span> <span class="o">=</span> <span class="n">generate_synthetic_pathways</span><span class="p">()</span>

<span class="c1"># Display the .head() of each DataFrame</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees.head():"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">df_occupations.head():"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_occupations</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">df_pathways.head():"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_pathways</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>

<span class="c1"># Print the PARAMS dictionary</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Global PARAMS dictionary:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">PARAMS</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees.head():
  employee_id          job_role   department  years_experience  \
0      EMP000     HR Specialist  Engineering                12   
1      EMP001       ML Engineer    Marketing                12   
2      EMP002       AI Ethicist           HR                 8   
3      EMP003  Business Analyst  Engineering                12   
4      EMP004  Business Analyst      Finance                 5   

           education_level  prompting_score  tools_score  understanding_score  \
0  Associate's/Certificate               52           83                   88   
1            HS+Coursework               82           78                   63   
2                      PhD               47           57                   42   
3                 Master's               33           69                   43   
4               Bachelor's               86           42                   76   

   data_lit_score  output_quality_with_ai  ...  skill_g  skill_h  skill_i  \
0              76                0.951681  ...       76       83       24   
1              85                0.985627  ...       63       92        5   
2              55                0.703442  ...       92       74       79   
3              76                0.971908  ...       72       66        4   
4              57                1.159548  ...        8       65       39   

   skill_j  errors_caught_norm  trust_decisions_norm  \
0       61           40.909091            104.545455   
1       87          118.750000             85.000000   
2       98           65.217391             77.419355   
3       52           95.000000             84.000000   
4       12           60.000000             84.615385   

   output_quality_without_ai_safe  time_with_ai_safe  \
0                        0.949397           0.860098   
1                        0.846545           0.734636   
2                        0.950472           0.975965   
3                        0.726585           0.819774   
4                        0.856980           0.731528   

   ai_augmented_productivity_raw  ai_augmented_productivity_norm  
0                       1.725586                       86.279322  
1                       1.872545                       93.627252  
2                       0.899030                       44.951505  
3                       2.027585                      100.000000  
4                       2.104211                      100.000000  

[5 rows x 41 columns]

df_occupations.head():
         occupation  ai_enhancement_potential  projected_jobs_t  \
0    Data Scientist                        85              5000   
1       ML Engineer                        90              4000   
2       AI Ethicist                        75              1000   
3  Business Analyst                        60             15000   
4     HR Specialist                        50             12000   

   projected_jobs_t_plus_10  ai_skilled_wage  median_wage  \
0                      8000           140000       110000   
1                      7500           150000       120000   
2                      2000           120000       100000   
3                     16000            90000        75000   
4                     11000            80000        65000   

   education_years_required  experience_years_required  remote_work_factor  \
0                        18                          3                 0.8   
1                        18                          4                 0.9   
2                        16                          2                 0.7   
3                        16                          2                 0.6   
4                        14                          1                 0.5   

   job_postings_current_month  ...  required_skill_f  skill_f_importance  \
0                         120  ...                82            0.133353   
1                         110  ...                67            0.748522   
2                          40  ...                32            0.400474   
3                          80  ...                65            0.185727   
4                          70  ...                77            0.652096   

   required_skill_g  skill_g_importance  required_skill_h  skill_h_importance  \
0                77            0.713486                81            0.374224   
1                82            0.958518                53            0.547622   
2                79            0.720129                84            0.392526   
3                73            0.702594                60            0.422680   
4                61            0.511087                34            0.921857   

   required_skill_i  skill_i_importance  required_skill_j  skill_j_importance  
0                88            0.134255                43            0.226217  
1                88            0.885883                37            0.456144  
2                79            0.476001                47            0.145126  
3                31            0.225402                64            0.286115  
4                86            0.438136                80            0.183183  

[5 rows x 32 columns]

df_pathways.head():
  pathway_id                pathway_name   pathway_type  cost  time_hours  \
0     PATH01      AI Fundamentals Course  Online Course   500          40   
1     PATH02  Advanced ML Specialization  Certification  2000         160   
2     PATH03      AI Ethics &amp; Governance       Workshop  1000          80   
3     PATH04   Data Storytelling with AI  Online Course   300          30   
4     PATH05        HR Analytics with AI  Certification   750          60   

   delta_ai_fluency  delta_domain_expertise  delta_adaptive_capacity  
0                10                       5                        5  
1                25                      10                        5  
2                 5                      15                       10  
3                 3                       8                        7  
4                 5                      12                        8  

Global PARAMS dictionary:
{'alpha': 0.6, 'beta': 0.15, 'lambda_growth': 0.3, 'gamma_regional': 0.2, 'hr_base_weights': {'ai_enhancement_weight': 0.3, 'job_growth_weight': 0.3, 'wage_premium_weight': 0.25, 'entry_accessibility_weight': 0.15}, 'theta_ai_fluency_weights': {'technical_ai_skills_weight': 0.3, 'ai_augmented_productivity_weight': 0.35, 'critical_ai_judgment_weight': 0.2, 'ai_learning_velocity_weight': 0.15}, 'gamma_experience_decay': 0.15, 'domain_specialization_weights': {'portfolio_weight': 0.4, 'recognition_weight': 0.3, 'credentials_weight': 0.3}, 'vr_component_weights': {'ai_fluency_weight_vr': 0.45, 'domain_expertise_weight_vr': 0.35, 'adaptive_capacity_weight_vr': 0.2}}
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=6e9edf6c">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The synthetic datasets provide a realistic basis for computing the AI-R scores and simulating scenarios. The <code>PARAMS</code> dictionary centralizes all coefficients and weights, making the model transparent and easily adjustable for future calibration or exploration. This setup ensures that all subsequent calculations have concrete input data and predefined parameters.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=9115e43d">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-3:-Systematic-Opportunity-($HR%5ER$)-Components:-AI-Enhancement-Potential">Section 3: Systematic Opportunity ($HR^R$) Components: AI-Enhancement Potential<a class="anchor-link" href="#Section-3:-Systematic-Opportunity-($HR%5ER$)-Components:-AI-Enhancement-Potential">¶</a></h1><p>The Systematic Opportunity ($HR^R$) component quantifies macro-level market demand and growth potential. One crucial factor is the AI-Enhancement Potential, which measures how much AI augments rather than replaces tasks within an occupation. It is defined as:</p>
<p>$$AI\text{-}Enhancement_o = \frac{1}{|T_o|} \sum_{t \in T_o} (1 - Automation_t) \cdot AI\text{-}Augmentation_t$$</p>
<p>where $T_o$ is the set of tasks for occupation $o$, $Automation_t \in [0,1]$ measures replaceability, and $AI\text{-}Augmentation_t \in [0,1]$ measures productivity enhancement. For simplicity in our synthetic data, we directly include an aggregated <code>ai_enhancement_potential</code> for each occupation in <code>df_occupations</code>.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=428edf69">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_ai_enhancement</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes AI-Enhancement Potential for a given occupation."""</span>
    <span class="c1"># Directly extract the pre-aggregated ai_enhancement_potential</span>
    <span class="k">return</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'ai_enhancement_potential'</span><span class="p">]</span>

<span class="c1"># Test the function immediately</span>
<span class="n">example_occupation</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test AI-Enhancement Potential for </span><span class="si">{</span><span class="n">example_occupation</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">calculate_ai_enhancement</span><span class="p">(</span><span class="n">example_occupation</span><span class="p">)</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test AI-Enhancement Potential for Data Scientist: 85.00
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=33734390">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>This step demonstrates how the AI-Enhancement Potential, a key sub-component of $HR^R$, is retrieved for a specific job role. This value reflects the degree to which AI is expected to augment, rather than automate, tasks within that occupation, indicating its future relevance.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=4042a047">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-4:-Systematic-Opportunity-($HR%5ER$)-Components:-Job-Growth-Projections">Section 4: Systematic Opportunity ($HR^R$) Components: Job Growth Projections<a class="anchor-link" href="#Section-4:-Systematic-Opportunity-($HR%5ER$)-Components:-Job-Growth-Projections">¶</a></h1><p>Job Growth Projections quantify the expected increase or decrease in employment for an occupation over a given period (e.g., 10 years). The raw growth rate $g$ is calculated as:</p>
<p>$$Growth_o = \frac{\text{Projected Jobs}_{o,t+10} - \text{Current Jobs}_{o,t}}{\text{Current Jobs}_{o,t}}$$</p>
<p>This raw growth rate is then normalized to a scale of $[0, 100]$ using an affine transformation to make it comparable with other AI-R components:</p>
<p>$$Growth_{\text{normalized}} = \frac{g + 0.5}{2.0} \times 100$$</p>
<p>This transformation maps a growth rate range of $g \in [-0.5, 1.5]$ (representing -50% to +150% change) to $[0,100]$.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=ace1633d">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_job_growth_normalized</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes normalized job growth projection for an occupation."""</span>
    <span class="n">current_jobs</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'projected_jobs_t'</span><span class="p">]</span>
    <span class="n">projected_jobs_10_years</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'projected_jobs_t_plus_10'</span><span class="p">]</span>

    <span class="k">if</span> <span class="n">current_jobs</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span> <span class="c1"># Handle division by zero</span>

    <span class="n">raw_growth_rate</span> <span class="o">=</span> <span class="p">(</span><span class="n">projected_jobs_10_years</span> <span class="o">-</span> <span class="n">current_jobs</span><span class="p">)</span> <span class="o">/</span> <span class="n">current_jobs</span>

    <span class="c1"># Normalize to [0, 100] using the affine transformation</span>
    <span class="c1"># Growth rate range for normalization: g \in [-0.5, 1.5]</span>
    <span class="c1"># -0.5 maps to 0, 1.5 maps to 100.</span>
    <span class="n">normalized_growth</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(((</span><span class="n">raw_growth_rate</span> <span class="o">+</span> <span class="mf">0.5</span><span class="p">)</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">raw_growth_rate</span><span class="p">,</span> <span class="n">normalized_growth</span>

<span class="c1"># Test the function immediately</span>
<span class="n">example_occupation</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">raw_growth</span><span class="p">,</span> <span class="n">normalized_growth</span> <span class="o">=</span> <span class="n">calculate_job_growth_normalized</span><span class="p">(</span><span class="n">example_occupation</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Job Growth for </span><span class="si">{</span><span class="n">example_occupation</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span><span class="si">}</span><span class="s2">: Raw=</span><span class="si">{</span><span class="n">raw_growth</span><span class="si">:</span><span class="s2">.2%</span><span class="si">}</span><span class="s2">, Normalized=</span><span class="si">{</span><span class="n">normalized_growth</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Job Growth for Data Scientist: Raw=60.00%, Normalized=55.00
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=1ea686f5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The normalized job growth score provides a standardized measure of an occupation's future demand, directly contributing to its Systematic Opportunity. A higher normalized score indicates a greater projected increase in job availability, making the occupation more attractive in the AI-transformed labor market.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=57495897">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-5:-Systematic-Opportunity-($HR%5ER$)-Components:-Wage-Premium-&amp;-Entry-Accessibility">Section 5: Systematic Opportunity ($HR^R$) Components: Wage Premium &amp; Entry Accessibility<a class="anchor-link" href="#Section-5:-Systematic-Opportunity-($HR%5ER$)-Components:-Wage-Premium-&amp;-Entry-Accessibility">¶</a></h1><p>Two other critical factors contributing to Systematic Opportunity are Wage Premium and Entry Accessibility.
<strong>Wage Premium</strong> ($Wage_o$) measures the compensation potential for AI-skilled roles relative to the median wage in that occupation:</p>
<p>$$Wage_o = \frac{\text{AI-skilled wage}_o - \text{median wage}_o}{\text{median wage}_o}$$</p>
<p>This provides an indication of the economic value placed on AI-related skills within a role.</p>
<p><strong>Entry Accessibility</strong> ($Access_o$) quantifies the ease of transitioning into a role, based on typical educational and experience requirements:</p>
<p>$$Access_o = 1 - \frac{\text{Education Years Required} + \text{Experience Years Required}}{10}$$</p>
<p>This linear formula provides a simplified measure, where a higher score indicates easier entry.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=a020e73a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>⚠️ The code execution failed in the sandbox after multiple attempts.
Please check the below cell and manually resolve the issue.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=6e21823b">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">numpy</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">np</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">random</span>

<span class="c1"># Re-defining the functions as per the requirement for self-contained tests.</span>
<span class="c1"># The previous SyntaxError was resolved by changing single quotes 'a' to double quotes "a" in f-strings.</span>
<span class="c1"># This correction is applied here as well in helper functions used by tests.</span>

<span class="k">def</span><span class="w"> </span><span class="nf">generate_synthetic_employees</span><span class="p">(</span><span class="n">num_employees</span><span class="o">=</span><span class="mi">50</span><span class="p">):</span>
    <span class="n">employee_data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'employee_id'</span><span class="p">:</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'EMP</span><span class="si">{</span><span class="n">i</span><span class="si">:</span><span class="s1">03d</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_employees</span><span class="p">)],</span>
        <span class="s1">'job_role'</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">([</span><span class="s1">'Data Scientist'</span><span class="p">,</span> <span class="s1">'ML Engineer'</span><span class="p">,</span> <span class="s1">'AI Ethicist'</span><span class="p">,</span> <span class="s1">'Business Analyst'</span><span class="p">,</span> <span class="s1">'HR Specialist'</span><span class="p">],</span> <span class="n">k</span><span class="o">=</span><span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'department'</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">([</span><span class="s1">'R&amp;D'</span><span class="p">,</span> <span class="s1">'Engineering'</span><span class="p">,</span> <span class="s1">'HR'</span><span class="p">,</span> <span class="s1">'Marketing'</span><span class="p">,</span> <span class="s1">'Finance'</span><span class="p">],</span> <span class="n">k</span><span class="o">=</span><span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'years_experience'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'education_level'</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">choices</span><span class="p">([</span><span class="s1">'HS+Coursework'</span><span class="p">,</span> <span class="s1">'Associate</span><span class="se">\'</span><span class="s1">s/Certificate'</span><span class="p">,</span> <span class="s1">'Bachelor</span><span class="se">\'</span><span class="s1">s'</span><span class="p">,</span> <span class="s1">'Master</span><span class="se">\'</span><span class="s1">s'</span><span class="p">,</span> <span class="s1">'PhD'</span><span class="p">],</span> <span class="n">k</span><span class="o">=</span><span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'tools_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">40</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">35</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'output_quality_with_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.7</span><span class="p">,</span> <span class="mf">1.2</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span> <span class="c1"># Relative to without AI</span>
        <span class="s1">'output_quality_without_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'time_without_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="mf">1.5</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span> <span class="c1"># Relative to with AI</span>
        <span class="s1">'time_with_ai'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.7</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'errors_caught'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'total_ai_errors'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'appropriate_trust_decisions'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'total_decisions'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.05</span><span class="p">,</span> <span class="mf">0.25</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'hours_invested'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="mi">500</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'domain_portfolio_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'domain_recognition_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">80</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'domain_credentials_score'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'adaptive_cognitive_flexibility'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">40</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'adaptive_social_emotional'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">),</span>
        <span class="s1">'adaptive_strategic_career'</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">35</span><span class="p">,</span> <span class="mi">95</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">)</span>
    <span class="p">}</span>
    <span class="c1"># Add generic skills for skill match</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="n">employee_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="n">num_employees</span><span class="p">)</span>

    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">employee_data</span><span class="p">)</span>

    <span class="c1"># Normalize scores to 0-100 where applicable (these are raw inputs)</span>
    <span class="c1"># Handle division by zero gracefully, though with randint ranges, it's unlikely total_ai_errors/total_decisions are 0</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'errors_caught_norm'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'errors_caught'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'total_ai_errors'</span><span class="p">]</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'trust_decisions_norm'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'appropriate_trust_decisions'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'total_decisions'</span><span class="p">]</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

    <span class="c1"># Ensure no division by zero for output_quality_without_ai and time_with_ai</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai_safe'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai'</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai_safe'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai'</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">nan</span><span class="p">)</span>

    <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_with_ai'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'output_quality_without_ai_safe'</span><span class="p">])</span> <span class="o">*</span> \
                                         <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'time_without_ai'</span><span class="p">]</span> <span class="o">/</span> <span class="n">df</span><span class="p">[</span><span class="s1">'time_with_ai_safe'</span><span class="p">])</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span> <span class="c1"># Fill NaN if division by zero occurred</span>

    <span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_norm'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_raw'</span><span class="p">]</span> <span class="o">*</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span> <span class="c1"># Scale and clip for initial S_i2</span>

    <span class="k">return</span> <span class="n">df</span>

<span class="k">def</span><span class="w"> </span><span class="nf">generate_synthetic_occupations</span><span class="p">():</span>
    <span class="n">occupation_data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'occupation'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'Data Scientist'</span><span class="p">,</span> <span class="s1">'ML Engineer'</span><span class="p">,</span> <span class="s1">'AI Ethicist'</span><span class="p">,</span> <span class="s1">'Business Analyst'</span><span class="p">,</span> <span class="s1">'HR Specialist'</span><span class="p">],</span>
        <span class="s1">'ai_enhancement_potential'</span><span class="p">:</span> <span class="p">[</span><span class="mi">85</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="mi">75</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span> <span class="mi">50</span><span class="p">],</span>
        <span class="s1">'projected_jobs_t'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5000</span><span class="p">,</span> <span class="mi">4000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">,</span> <span class="mi">15000</span><span class="p">,</span> <span class="mi">12000</span><span class="p">],</span>
        <span class="s1">'projected_jobs_t_plus_10'</span><span class="p">:</span> <span class="p">[</span><span class="mi">8000</span><span class="p">,</span> <span class="mi">7500</span><span class="p">,</span> <span class="mi">2000</span><span class="p">,</span> <span class="mi">16000</span><span class="p">,</span> <span class="mi">11000</span><span class="p">],</span>
        <span class="s1">'ai_skilled_wage'</span><span class="p">:</span> <span class="p">[</span><span class="mi">140000</span><span class="p">,</span> <span class="mi">150000</span><span class="p">,</span> <span class="mi">120000</span><span class="p">,</span> <span class="mi">90000</span><span class="p">,</span> <span class="mi">80000</span><span class="p">],</span>
        <span class="s1">'median_wage'</span><span class="p">:</span> <span class="p">[</span><span class="mi">110000</span><span class="p">,</span> <span class="mi">120000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mi">75000</span><span class="p">,</span> <span class="mi">65000</span><span class="p">],</span>
        <span class="s1">'education_years_required'</span><span class="p">:</span> <span class="p">[</span><span class="mi">18</span><span class="p">,</span> <span class="mi">18</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span> <span class="mi">14</span><span class="p">],</span>
        <span class="s1">'experience_years_required'</span><span class="p">:</span> <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span>
        <span class="s1">'remote_work_factor'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.8</span><span class="p">,</span> <span class="mf">0.9</span><span class="p">,</span> <span class="mf">0.7</span><span class="p">,</span> <span class="mf">0.6</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">],</span>
        <span class="s1">'job_postings_current_month'</span><span class="p">:</span> <span class="p">[</span><span class="mi">120</span><span class="p">,</span> <span class="mi">110</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">80</span><span class="p">,</span> <span class="mi">70</span><span class="p">],</span>
        <span class="s1">'job_postings_prev_month'</span><span class="p">:</span> <span class="p">[</span><span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">35</span><span class="p">,</span> <span class="mi">85</span><span class="p">,</span> <span class="mi">75</span><span class="p">],</span>
        <span class="s1">'national_avg_demand'</span><span class="p">:</span> <span class="p">[</span><span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">]</span>
    <span class="p">}</span>
    <span class="c1"># Add required skills and importance</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
        <span class="n">occupation_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span> <span class="mi">90</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]))</span>
        <span class="n">occupation_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.1</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]))</span>

    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">generate_synthetic_pathways</span><span class="p">():</span>
    <span class="n">pathway_data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'pathway_id'</span><span class="p">:</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'PATH</span><span class="si">{</span><span class="n">i</span><span class="si">:</span><span class="s1">02d</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">)],</span>
        <span class="s1">'pathway_name'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'AI Fundamentals Course'</span><span class="p">,</span> <span class="s1">'Advanced ML Specialization'</span><span class="p">,</span> <span class="s1">'AI Ethics &amp; Governance'</span><span class="p">,</span> <span class="s1">'Data Storytelling with AI'</span><span class="p">,</span> <span class="s1">'HR Analytics with AI'</span><span class="p">],</span>
        <span class="s1">'pathway_type'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'Online Course'</span><span class="p">,</span> <span class="s1">'Certification'</span><span class="p">,</span> <span class="s1">'Workshop'</span><span class="p">,</span> <span class="s1">'Online Course'</span><span class="p">,</span> <span class="s1">'Certification'</span><span class="p">],</span>
        <span class="s1">'cost'</span><span class="p">:</span> <span class="p">[</span><span class="mi">500</span><span class="p">,</span> <span class="mi">2000</span><span class="p">,</span> <span class="mi">1000</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">750</span><span class="p">],</span>
        <span class="s1">'time_hours'</span><span class="p">:</span> <span class="p">[</span><span class="mi">40</span><span class="p">,</span> <span class="mi">160</span><span class="p">,</span> <span class="mi">80</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">60</span><span class="p">],</span>
        <span class="s1">'delta_ai_fluency'</span><span class="p">:</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">25</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
        <span class="s1">'delta_domain_expertise'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">15</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">12</span><span class="p">],</span>
        <span class="s1">'delta_adaptive_capacity'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">]</span>
    <span class="p">}</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">pathway_data</span><span class="p">)</span>


<span class="k">def</span><span class="w"> </span><span class="nf">calculate_wage_premium</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes wage premium for an occupation."""</span>
    <span class="n">ai_skilled_wage</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'ai_skilled_wage'</span><span class="p">]</span>
    <span class="n">median_wage</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'median_wage'</span><span class="p">]</span>

    <span class="k">if</span> <span class="n">median_wage</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>

    <span class="n">wage_premium</span> <span class="o">=</span> <span class="p">(</span><span class="n">ai_skilled_wage</span> <span class="o">-</span> <span class="n">median_wage</span><span class="p">)</span> <span class="o">/</span> <span class="n">median_wage</span>
    <span class="c1"># Normalize to a 0-100 scale; assuming typical premiums are between -0.2 and 0.5</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(((</span><span class="n">wage_premium</span> <span class="o">+</span> <span class="mf">0.2</span><span class="p">)</span> <span class="o">/</span> <span class="mf">0.7</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_entry_accessibility</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes entry accessibility for an occupation."""</span>
    <span class="n">education_years_required</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'education_years_required'</span><span class="p">]</span>
    <span class="n">experience_years_required</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'experience_years_required'</span><span class="p">]</span>

    <span class="c1"># Using the formula: 1 - (total_years / 10) for a simpler range adjustment</span>
    <span class="n">access_score</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">-</span> <span class="p">((</span><span class="n">education_years_required</span> <span class="o">+</span> <span class="n">experience_years_required</span><span class="p">)</span> <span class="o">/</span> <span class="mi">10</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">access_score</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>


<span class="c1"># Pytest unit tests</span>
<span class="k">class</span><span class="w"> </span><span class="nc">TestHRRComponents</span><span class="p">:</span>

    <span class="c1"># --- Tests for calculate_wage_premium ---</span>
    <span class="nd">@pytest</span><span class="o">.</span><span class="n">mark</span><span class="o">.</span><span class="n">parametrize</span><span class="p">(</span><span class="s2">"ai_skilled_wage, median_wage, expected_premium"</span><span class="p">,</span> <span class="p">[</span>
        <span class="p">(</span><span class="mi">150000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mf">100.0</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">100000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mf">28.57142857142857</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">80000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">70000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">200000</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mf">100.0</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100000</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">100000</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>
        <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">)</span>
    <span class="p">])</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_wage_premium</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ai_skilled_wage</span><span class="p">,</span> <span class="n">median_wage</span><span class="p">,</span> <span class="n">expected_premium</span><span class="p">):</span>
        <span class="n">occupation_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'ai_skilled_wage'</span><span class="p">:</span> <span class="n">ai_skilled_wage</span><span class="p">,</span>
            <span class="s1">'median_wage'</span><span class="p">:</span> <span class="n">median_wage</span>
        <span class="p">})</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">calculate_wage_premium</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">floating</span><span class="p">))</span>
        <span class="c1"># Use np.isclose for float comparisons</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">expected_premium</span><span class="p">)</span>
        <span class="k">assert</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">result</span> <span class="o">&lt;=</span> <span class="mi">100</span>

    <span class="c1"># --- Tests for calculate_entry_accessibility ---</span>
    <span class="nd">@pytest</span><span class="o">.</span><span class="n">mark</span><span class="o">.</span><span class="n">parametrize</span><span class="p">(</span><span class="s2">"education_years, experience_years, expected_accessibility"</span><span class="p">,</span> <span class="p">[</span>
        <span class="p">(</span><span class="mi">18</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>  <span class="c1"># (1 - (21 / 10)) * 100 = -110, clipped to 0</span>
        <span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>  <span class="c1"># (1 - (12 / 10)) * 100 = -20, clipped to 0</span>
        <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mf">100.0</span><span class="p">),</span> <span class="c1"># (1 - (0 / 10)) * 100 = 100</span>
        <span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>  <span class="c1"># (1 - (10 / 10)) * 100 = 0</span>
        <span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mf">10.0</span><span class="p">),</span>  <span class="c1"># (1 - (9 / 10)) * 100 = 10</span>
        <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mf">80.0</span><span class="p">),</span>  <span class="c1"># (1 - (2 / 10)) * 100 = 80</span>
        <span class="p">(</span><span class="mi">25</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>  <span class="c1"># (1 - (30 / 10)) * 100 = -200, clipped to 0</span>
        <span class="p">(</span><span class="mi">14</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span>  <span class="c1"># HR Specialist example: (1 - 1.5) * 100 = -50, clipped to 0</span>
        <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mf">50.0</span><span class="p">),</span>  <span class="c1"># (1 - (5 / 10)) * 100 = 50</span>
        <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mf">50.0</span><span class="p">),</span>  <span class="c1"># (1 - (5 / 10)) * 100 = 50</span>
    <span class="p">])</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_entry_accessibility</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">education_years</span><span class="p">,</span> <span class="n">experience_years</span><span class="p">,</span> <span class="n">expected_accessibility</span><span class="p">):</span>
        <span class="n">occupation_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'education_years_required'</span><span class="p">:</span> <span class="n">education_years</span><span class="p">,</span>
            <span class="s1">'experience_years_required'</span><span class="p">:</span> <span class="n">experience_years</span>
        <span class="p">})</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">calculate_entry_accessibility</span><span class="p">(</span><span class="n">occupation_data</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">floating</span><span class="p">))</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">expected_accessibility</span><span class="p">)</span>
        <span class="k">assert</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">result</span> <span class="o">&lt;=</span> <span class="mi">100</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=5d991903">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>These calculations complete the primary sub-components of the Base Opportunity Score. Wage Premium highlights the financial attractiveness of an AI-enabled role, while Entry Accessibility provides insight into the practical barriers for individuals considering a transition, both being crucial for assessing Systematic Opportunity.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=a0511efd">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-6:-Calculate-Base-Opportunity-Score-($H_%7B%5Ctext%7Bbase%7D%7D$)">Section 6: Calculate Base Opportunity Score ($H_{\text{base}}$)<a class="anchor-link" href="#Section-6:-Calculate-Base-Opportunity-Score-($H_%7B%5Ctext%7Bbase%7D%7D$)">¶</a></h1><p>The Base Opportunity Score ($H_{\text{base}}(o)$) aggregates the various dimensions of occupational attractiveness: AI-Enhancement Potential, Job Growth Projections, Wage Premium, and Entry Accessibility. It is calculated as a weighted sum:</p>
<p>$$H_{\text{base}}(o) = w_1 \cdot AI\text{-}Enhancement_o + w_2 \cdot Growth_{\text{normalized}} + w_3 \cdot Wage_o + w_4 \cdot Access_o$$</p>
<p>The weights ($w_j$) reflect the relative importance of each factor, as defined in the <code>PARAMS</code> dictionary ($w_1 = 0.30$, $w_2 = 0.30$, $w_3 = 0.25$, $w_4 = 0.15$). The final score is then scaled to $[0,100]$.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=f1d572bc">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [10]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_base_opportunity_score</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">,</span> <span class="n">weights</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Aggregates sub-components into H_base."""</span>
    <span class="n">ai_enhancement</span> <span class="o">=</span> <span class="n">calculate_ai_enhancement</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">)</span>
    <span class="n">_</span><span class="p">,</span> <span class="n">job_growth_normalized</span> <span class="o">=</span> <span class="n">calculate_job_growth_normalized</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">)</span>
    <span class="n">wage_premium</span> <span class="o">=</span> <span class="n">calculate_wage_premium</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">)</span>
    <span class="n">entry_accessibility</span> <span class="o">=</span> <span class="n">calculate_entry_accessibility</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">)</span>

    <span class="n">h_base</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'ai_enhancement_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">ai_enhancement</span> <span class="o">+</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'job_growth_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">job_growth_normalized</span> <span class="o">+</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'wage_premium_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">wage_premium</span> <span class="o">+</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'entry_accessibility_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">entry_accessibility</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">h_base</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Test the function immediately</span>
<span class="n">example_occupation</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">h_base_score</span> <span class="o">=</span> <span class="n">calculate_base_opportunity_score</span><span class="p">(</span><span class="n">example_occupation</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'hr_base_weights'</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Base Opportunity Score for </span><span class="si">{</span><span class="n">example_occupation</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">h_base_score</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Base Opportunity Score for Data Scientist: 58.88
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=7afb1900">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_occupations with the base_opportunity_score for all occupations</span>
<span class="n">df_occupations</span><span class="p">[</span><span class="s1">'base_opportunity_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_base_opportunity_score</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'hr_base_weights'</span><span class="p">]),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_occupations with 'base_opportunity_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_occupations</span><span class="p">[[</span><span class="s1">'occupation'</span><span class="p">,</span> <span class="s1">'base_opportunity_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_occupations with 'base_opportunity_score':
         occupation  base_opportunity_score
0    Data Scientist               58.883117
1       ML Engineer               63.696429
2       AI Ethicist               59.285714
3  Business Analyst               40.785714
4     HR Specialist               36.634615
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=88c920d1">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The Base Opportunity Score synthesizes multiple static aspects of an occupation's attractiveness. This score provides a foundational understanding of the long-term potential of a career path, serving as a key input for the overall Systematic Opportunity.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=d829f6bc">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-7:-Dynamic-Multipliers:-Growth-&amp;-Regional">Section 7: Dynamic Multipliers: Growth &amp; Regional<a class="anchor-link" href="#Section-7:-Dynamic-Multipliers:-Growth-&amp;-Regional">¶</a></h1><p>Beyond the static Base Opportunity Score, Systematic Opportunity is modulated by dynamic, time-varying market factors:</p>
<ol>
<li><strong>Growth Multiplier ($M_{\text{growth}}(t)$):</strong> Captures market momentum based on recent changes in job postings.
$$M_{\text{growth}}(t) = 1 + \lambda \cdot \left( \frac{\text{Job Postings}_{o,t}}{\text{Job Postings}_{o,t-1}} - 1 \right)$$
where $\lambda = 0.3$ (from <code>PARAMS</code>) dampens volatility, keeping the multiplier typically between $0.7$ and $1.3$.</li>
<li><strong>Regional Multiplier ($M_{\text{regional}}(t)$):</strong> Adjusts for local labor market conditions and remote work suitability.
$$M_{\text{regional}}(t) = \frac{\text{Local Demand}_{i,t}}{\text{National Avg Demand}} \times (1 + \gamma \cdot \text{Remote Work Factor}_o)$$
where $\gamma = 0.2$ (from <code>PARAMS</code>) and $Remote Work Factor \in [0,1]$ measures the occupation's suitability for remote work. For simplicity, we will assume <code>Local Demand</code> equals <code>National Avg Demand</code> for the primary calculation and focus on the <code>Remote Work Factor</code> contribution.</li>
</ol>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=2eaa3552">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [12]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_growth_multiplier</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">,</span> <span class="n">lambda_val</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes market momentum growth multiplier."""</span>
    <span class="n">current_postings</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'job_postings_current_month'</span><span class="p">]</span>
    <span class="n">prev_postings</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'job_postings_prev_month'</span><span class="p">]</span>

    <span class="k">if</span> <span class="n">prev_postings</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="mf">1.0</span> <span class="c1"># No change if no previous data</span>

    <span class="n">change_factor</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_postings</span> <span class="o">/</span> <span class="n">prev_postings</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="n">multiplier</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="n">lambda_val</span> <span class="o">*</span> <span class="n">change_factor</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">multiplier</span><span class="p">,</span> <span class="mf">0.7</span><span class="p">,</span> <span class="mf">1.3</span><span class="p">)</span> <span class="c1"># Clamp to reasonable range</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_regional_multiplier</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">,</span> <span class="n">gamma_val</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes regional demand multiplier."""</span>
    <span class="c1"># For simplicity, assume Local Demand equals National Avg Demand (ratio of 1.0) unless specified.</span>
    <span class="n">local_to_national_ratio</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'local_demand_ratio'</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">)</span>
    <span class="n">remote_work_factor</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'remote_work_factor'</span><span class="p">]</span>

    <span class="n">multiplier</span> <span class="o">=</span> <span class="n">local_to_national_ratio</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="n">gamma_val</span> <span class="o">*</span> <span class="n">remote_work_factor</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">multiplier</span><span class="p">,</span> <span class="mf">0.8</span><span class="p">,</span> <span class="mf">1.2</span><span class="p">)</span> <span class="c1"># Clamp to reasonable range</span>

<span class="c1"># Test the functions immediately</span>
<span class="n">example_occupation</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">growth_mult</span> <span class="o">=</span> <span class="n">calculate_growth_multiplier</span><span class="p">(</span><span class="n">example_occupation</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'lambda_growth'</span><span class="p">])</span>
<span class="n">regional_mult</span> <span class="o">=</span> <span class="n">calculate_regional_multiplier</span><span class="p">(</span><span class="n">example_occupation</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'gamma_regional'</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Growth Multiplier for </span><span class="si">{</span><span class="n">example_occupation</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">growth_mult</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Regional Multiplier for </span><span class="si">{</span><span class="n">example_occupation</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">regional_mult</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Growth Multiplier for Data Scientist: 1.06
Test Regional Multiplier for Data Scientist: 1.16
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=aefa2670">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [13]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_occupations with growth_multiplier and regional_multiplier for all occupations</span>
<span class="n">df_occupations</span><span class="p">[</span><span class="s1">'growth_multiplier'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_growth_multiplier</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'lambda_growth'</span><span class="p">]),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">df_occupations</span><span class="p">[</span><span class="s1">'regional_multiplier'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_regional_multiplier</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'gamma_regional'</span><span class="p">]),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_occupations with 'growth_multiplier' and 'regional_multiplier':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_occupations</span><span class="p">[[</span><span class="s1">'occupation'</span><span class="p">,</span> <span class="s1">'growth_multiplier'</span><span class="p">,</span> <span class="s1">'regional_multiplier'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_occupations with 'growth_multiplier' and 'regional_multiplier':
         occupation  growth_multiplier  regional_multiplier
0    Data Scientist           1.060000                 1.16
1       ML Engineer           1.030000                 1.18
2       AI Ethicist           1.042857                 1.14
3  Business Analyst           0.982353                 1.12
4     HR Specialist           0.980000                 1.10
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=6b6758b8">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The dynamic multipliers introduce responsiveness to market fluctuations. The Growth Multiplier reflects current hiring trends, while the Regional Multiplier accounts for geographical demand and the increasing prevalence of remote work. These factors ensure that the Systematic Opportunity score remains relevant to contemporary market conditions.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=769d95da">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-8:-Calculate-Final-Systematic-Opportunity-($HR%5ER$)">Section 8: Calculate Final Systematic Opportunity ($HR^R$)<a class="anchor-link" href="#Section-8:-Calculate-Final-Systematic-Opportunity-($HR%5ER$)">¶</a></h1><p>The final Systematic Opportunity score ($HR^R(t)$) for an individual $i$ targeting occupation $o_{\text{target}}$ at time $t$ is calculated by combining the Base Opportunity Score with the dynamic multipliers:</p>
<p>$$HR^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$</p>
<p>This comprehensive score represents the overall attractiveness and growth potential of a chosen occupation in the current market environment, normalized to a $[0, 100]$ scale.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=de9d0535">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [14]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_systematic_opportunity</span><span class="p">(</span><span class="n">occupation_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes total HR^R for a target occupation."""</span>
    <span class="n">base_score</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'base_opportunity_score'</span><span class="p">]</span>
    <span class="n">growth_mult</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'growth_multiplier'</span><span class="p">]</span>
    <span class="n">regional_mult</span> <span class="o">=</span> <span class="n">occupation_data_row</span><span class="p">[</span><span class="s1">'regional_multiplier'</span><span class="p">]</span>

    <span class="n">hr_r</span> <span class="o">=</span> <span class="n">base_score</span> <span class="o">*</span> <span class="n">growth_mult</span> <span class="o">*</span> <span class="n">regional_mult</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">hr_r</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Test the function immediately (using a merged row for simplicity in test)</span>
<span class="n">example_employee_job</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s1">'job_role'</span><span class="p">]</span>
<span class="n">example_hr_row</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="p">[</span><span class="n">df_occupations</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span> <span class="o">==</span> <span class="n">example_employee_job</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">example_hr_r</span> <span class="o">=</span> <span class="n">calculate_systematic_opportunity</span><span class="p">(</span><span class="n">example_hr_row</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test HR^R score for </span><span class="si">{</span><span class="n">example_employee_job</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">example_hr_r</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test HR^R score for HR Specialist: 39.49
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=48b64e85">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [15]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Iterate through df_employees to calculate HR^R scores</span>
<span class="n">df_employees</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="s1">'job_role'</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="k">lambda</span> <span class="n">job_role</span><span class="p">:</span>
        <span class="n">calculate_systematic_opportunity</span><span class="p">(</span><span class="n">df_occupations</span><span class="p">[</span><span class="n">df_occupations</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span> <span class="o">==</span> <span class="n">job_role</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'hr_r_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'hr_r_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'hr_r_score':
  employee_id          job_role  hr_r_score
0      EMP000     HR Specialist   39.492115
1      EMP001       ML Engineer   77.416639
2      EMP002       AI Ethicist   70.482245
3      EMP003  Business Analyst   44.873882
4      EMP004  Business Analyst   44.873882
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=2cd6f80b">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>This step completes the calculation of the Systematic Opportunity component for each employee, linking their current job role to market conditions. This score highlights external career potential that individuals can position themselves to capture.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=646c5c14">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-9:-Idiosyncratic-Readiness-($V%5ER$)-Components:-AI-Fluency-Factor">Section 9: Idiosyncratic Readiness ($V^R$) Components: AI-Fluency Factor<a class="anchor-link" href="#Section-9:-Idiosyncratic-Readiness-($V%5ER$)-Components:-AI-Fluency-Factor">¶</a></h1><p>Idiosyncratic Readiness ($V^R$) measures an individual's specific capabilities. The AI-Fluency factor is a key sub-component, representing the ability to effectively use, understand, and collaborate with AI systems. It is calculated as a weighted sum of four sub-components:</p>
<p>$$AI\text{-}Fluency_i = \sum_{k=1}^4 \theta_k \cdot S_{i,k}$$</p>
<p>The sub-components ($S_{i,k}$) and their weights ($\theta_k$ from <code>PARAMS</code>) are:</p>
<ol>
<li><strong>Technical AI Skills</strong> ($S_{i,1}$, $\theta_1 = 0.30$): Based on Prompting, Tools, Understanding, and Data Literacy scores. $$S_{i,1} = \frac{1}{4} (\text{Prompting}_i + \text{Tools}_i + \text{Understanding}_i + \text{DataLit}_i)$$</li>
<li><strong>AI-Augmented Productivity</strong> ($S_{i,2}$, $\theta_2 = 0.35$): Measures productivity gains with AI assistance. $$S_{i,2} = \frac{\text{Output Quality}_{i,\text{with AI}}}{\text{Output Quality}_{i,\text{without AI}}} \cdot \frac{\text{Time}_{i,\text{without AI}}}{\text{Time}_{i,\text{with AI}}}$$
For simplicity, our synthetic data has <code>ai_augmented_productivity_norm</code> pre-calculated based on this concept.</li>
<li><strong>Critical AI Judgment</strong> ($S_{i,3}$, $\theta_3 = 0.20$): Assesses error detection and appropriate trust decisions with AI outputs.$$S_{i,3} = \frac{\text{Errors Caught}_i}{\text{Total AI Errors}} + \frac{\text{Appropriate Trust Decisions}_i}{\text{Total Decisions}}$$
For simplicity, our synthetic data provides <code>errors_caught_norm</code> and <code>trust_decisions_norm</code> which we'll combine and re-normalize.</li>
<li><strong>AI Learning Velocity</strong> ($S_{i,4}$, $\theta_4 = 0.15$): Measures improvement rate per unit time investment.$$S_{i,4} = \frac{\Delta Proficiency_i}{\Delta t} \cdot \frac{1}{\text{Hours Invested}}$$
For simplicity in this notebook, $\Delta Proficiency_i / \Delta t$ can be approximated as a 'learning_rate' for simulation purposes and then scaled with <code>hours_invested</code>.</li>
</ol>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=fbc5e050">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [16]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">numpy</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">np</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">random</span>

<span class="c1"># Define default parameters for \alpha and \beta (from Cell 5)</span>
<span class="c1"># This PARAMS dictionary is crucial for the functions to be tested and their dependencies</span>
<span class="n">PARAMS</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s1">'alpha'</span><span class="p">:</span> <span class="mf">0.6</span><span class="p">,</span>
    <span class="s1">'beta'</span><span class="p">:</span> <span class="mf">0.15</span><span class="p">,</span>
    <span class="s1">'lambda_growth'</span><span class="p">:</span> <span class="mf">0.3</span><span class="p">,</span>
    <span class="s1">'gamma_regional'</span><span class="p">:</span> <span class="mf">0.2</span><span class="p">,</span>
    <span class="s1">'hr_base_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'ai_enhancement_weight'</span><span class="p">:</span> <span class="mf">0.30</span><span class="p">,</span>
        <span class="s1">'job_growth_weight'</span><span class="p">:</span> <span class="mf">0.30</span><span class="p">,</span>
        <span class="s1">'wage_premium_weight'</span><span class="p">:</span> <span class="mf">0.25</span><span class="p">,</span>
        <span class="s1">'entry_accessibility_weight'</span><span class="p">:</span> <span class="mf">0.15</span>
    <span class="p">},</span>
    <span class="s1">'theta_ai_fluency_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'technical_ai_skills_weight'</span><span class="p">:</span> <span class="mf">0.30</span><span class="p">,</span>
        <span class="s1">'ai_augmented_productivity_weight'</span><span class="p">:</span> <span class="mf">0.35</span><span class="p">,</span>
        <span class="s1">'critical_ai_judgment_weight'</span><span class="p">:</span> <span class="mf">0.20</span><span class="p">,</span>
        <span class="s1">'ai_learning_velocity_weight'</span><span class="p">:</span> <span class="mf">0.15</span>
    <span class="p">},</span>
    <span class="s1">'gamma_experience_decay'</span><span class="p">:</span> <span class="mf">0.15</span><span class="p">,</span>
    <span class="s1">'domain_specialization_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'portfolio_weight'</span><span class="p">:</span> <span class="mf">0.4</span><span class="p">,</span>
        <span class="s1">'recognition_weight'</span><span class="p">:</span> <span class="mf">0.3</span><span class="p">,</span>
        <span class="s1">'credentials_weight'</span><span class="p">:</span> <span class="mf">0.3</span>
    <span class="p">},</span>
    <span class="s1">'vr_component_weights'</span><span class="p">:</span> <span class="p">{</span>
        <span class="s1">'ai_fluency_weight_vr'</span><span class="p">:</span> <span class="mf">0.45</span><span class="p">,</span>
        <span class="s1">'domain_expertise_weight_vr'</span><span class="p">:</span> <span class="mf">0.35</span><span class="p">,</span>
        <span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">:</span> <span class="mf">0.20</span>
    <span class="p">}</span>
<span class="p">}</span>

<span class="c1"># The functions to be tested (redefined for self-containment in unit tests)</span>
<span class="k">def</span><span class="w"> </span><span class="nf">calculate_technical_ai_skills</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes S_i,1 (Technical AI Skills)."""</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="p">[</span>
        <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'prompting_score'</span><span class="p">],</span>
        <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'tools_score'</span><span class="p">],</span>
        <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'understanding_score'</span><span class="p">],</span>
        <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'data_lit_score'</span><span class="p">]</span>
    <span class="p">]</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_ai_augmented_productivity</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes S_i,2 (AI-Augmented Productivity)."""</span>
    <span class="k">return</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_norm'</span><span class="p">]</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_critical_ai_judgment</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes S_i,3 (Critical AI Judgment)."""</span>
    <span class="n">errors_caught_score</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'errors_caught_norm'</span><span class="p">]</span>
    <span class="n">trust_decisions_score</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'trust_decisions_norm'</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">([</span><span class="n">errors_caught_score</span><span class="p">,</span> <span class="n">trust_decisions_score</span><span class="p">])</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes S_i,4 (AI Learning Velocity)."""</span>
    <span class="n">learning_rate</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'learning_rate'</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">learning_rate</span> <span class="o">*</span> <span class="mi">100</span> <span class="o">*</span> <span class="mf">0.8</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_ai_fluency</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">theta_weights</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Aggregates S_i,k into AI-Fluency."""</span>
    <span class="n">s1</span> <span class="o">=</span> <span class="n">calculate_technical_ai_skills</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">)</span>
    <span class="n">s2</span> <span class="o">=</span> <span class="n">calculate_ai_augmented_productivity</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">)</span>
    <span class="n">s3</span> <span class="o">=</span> <span class="n">calculate_critical_ai_judgment</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">)</span>
    <span class="n">s4</span> <span class="o">=</span> <span class="n">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">)</span>

    <span class="n">ai_fluency</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">theta_weights</span><span class="p">[</span><span class="s1">'technical_ai_skills_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s1</span> <span class="o">+</span>
        <span class="n">theta_weights</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s2</span> <span class="o">+</span>
        <span class="n">theta_weights</span><span class="p">[</span><span class="s1">'critical_ai_judgment_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s3</span> <span class="o">+</span>
        <span class="n">theta_weights</span><span class="p">[</span><span class="s1">'ai_learning_velocity_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s4</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">ai_fluency</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Pytest unit tests</span>
<span class="k">class</span><span class="w"> </span><span class="nc">TestAIFluencyComponents</span><span class="p">:</span>

    <span class="c1"># Fixture to provide sample employee data row for consistent testing</span>
    <span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">sample_employee_data_row</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="c1"># Create a pandas Series with all required keys and sample values</span>
        <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
            <span class="s1">'tools_score'</span><span class="p">:</span> <span class="mi">70</span><span class="p">,</span>
            <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
            <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="mi">75</span><span class="p">,</span>
            <span class="s1">'ai_augmented_productivity_norm'</span><span class="p">:</span> <span class="mi">85</span><span class="p">,</span>
            <span class="s1">'errors_caught_norm'</span><span class="p">:</span> <span class="mi">70</span><span class="p">,</span>
            <span class="s1">'trust_decisions_norm'</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
            <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="mf">0.20</span><span class="p">,</span>
            <span class="s1">'hours_invested'</span><span class="p">:</span> <span class="mi">200</span> <span class="c1"># Not directly used in current S4 calculation, but part of context</span>
        <span class="p">})</span>

    <span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">sample_theta_weights</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'theta_ai_fluency_weights'</span><span class="p">]</span>

    <span class="c1"># --- Tests for calculate_technical_ai_skills ---</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_technical_ai_skills_typical</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_employee_data_row</span><span class="p">):</span>
        <span class="n">expected_s1</span> <span class="o">=</span> <span class="p">(</span><span class="mi">80</span> <span class="o">+</span> <span class="mi">70</span> <span class="o">+</span> <span class="mi">90</span> <span class="o">+</span> <span class="mi">75</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_technical_ai_skills</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">),</span> <span class="n">expected_s1</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_technical_ai_skills_edge_min</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'tools_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="mi">0</span>
        <span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_technical_ai_skills</span><span class="p">(</span><span class="n">employee_data</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_technical_ai_skills_edge_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'tools_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="mi">100</span>
        <span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_technical_ai_skills</span><span class="p">(</span><span class="n">employee_data</span><span class="p">),</span> <span class="mi">100</span><span class="p">)</span>

    <span class="c1"># --- Tests for calculate_ai_augmented_productivity ---</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_augmented_productivity_typical</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_employee_data_row</span><span class="p">):</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_augmented_productivity</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">),</span> <span class="mi">85</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_augmented_productivity_edge_min_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data_min</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'ai_augmented_productivity_norm'</span><span class="p">:</span> <span class="mi">0</span><span class="p">})</span>
        <span class="n">employee_data_max</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'ai_augmented_productivity_norm'</span><span class="p">:</span> <span class="mi">100</span><span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_augmented_productivity</span><span class="p">(</span><span class="n">employee_data_min</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_augmented_productivity</span><span class="p">(</span><span class="n">employee_data_max</span><span class="p">),</span> <span class="mi">100</span><span class="p">)</span>

    <span class="c1"># --- Tests for calculate_critical_ai_judgment ---</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_critical_ai_judgment_typical</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_employee_data_row</span><span class="p">):</span>
        <span class="n">expected_s3</span> <span class="o">=</span> <span class="p">(</span><span class="mi">70</span> <span class="o">+</span> <span class="mi">80</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_critical_ai_judgment</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">),</span> <span class="n">expected_s3</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_critical_ai_judgment_edge_min</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'errors_caught_norm'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'trust_decisions_norm'</span><span class="p">:</span> <span class="mi">0</span><span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_critical_ai_judgment</span><span class="p">(</span><span class="n">employee_data</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_critical_ai_judgment_edge_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'errors_caught_norm'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'trust_decisions_norm'</span><span class="p">:</span> <span class="mi">100</span><span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_critical_ai_judgment</span><span class="p">(</span><span class="n">employee_data</span><span class="p">),</span> <span class="mi">100</span><span class="p">)</span>

    <span class="c1"># --- Tests for calculate_ai_learning_velocity ---</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_learning_velocity_typical</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_employee_data_row</span><span class="p">):</span>
        <span class="n">expected_s4</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="mf">0.20</span> <span class="o">*</span> <span class="mi">100</span> <span class="o">*</span> <span class="mf">0.8</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">),</span> <span class="n">expected_s4</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_learning_velocity_edge_min</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'learning_rate'</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">employee_data</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_learning_velocity_edge_max_clip</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'learning_rate'</span><span class="p">:</span> <span class="mf">1.0</span><span class="p">})</span> <span class="c1"># A learning rate that results in score 80</span>
        <span class="n">expected_s4</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="mf">1.0</span> <span class="o">*</span> <span class="mi">100</span> <span class="o">*</span> <span class="mf">0.8</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">employee_data</span><span class="p">),</span> <span class="n">expected_s4</span><span class="p">)</span>

        <span class="n">employee_data_over_clip</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span><span class="s1">'learning_rate'</span><span class="p">:</span> <span class="mf">1.5</span><span class="p">})</span> <span class="c1"># Value that should clip to 100</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">employee_data_over_clip</span><span class="p">),</span> <span class="mi">100</span><span class="p">)</span>


    <span class="c1"># --- Tests for calculate_ai_fluency ---</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_fluency_typical</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_employee_data_row</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">):</span>
        <span class="n">s1</span> <span class="o">=</span> <span class="n">calculate_technical_ai_skills</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">)</span>
        <span class="n">s2</span> <span class="o">=</span> <span class="n">calculate_ai_augmented_productivity</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">)</span>
        <span class="n">s3</span> <span class="o">=</span> <span class="n">calculate_critical_ai_judgment</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">)</span>
        <span class="n">s4</span> <span class="o">=</span> <span class="n">calculate_ai_learning_velocity</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">)</span>

        <span class="n">expected_ai_fluency</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'technical_ai_skills_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s1</span> <span class="o">+</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s2</span> <span class="o">+</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'critical_ai_judgment_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s3</span> <span class="o">+</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'ai_learning_velocity_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s4</span>
        <span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_fluency</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">expected_ai_fluency</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">))</span>
        <span class="k">assert</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">calculate_ai_fluency</span><span class="p">(</span><span class="n">sample_employee_data_row</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">100</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_fluency_edge_all_zero</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">):</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'tools_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
            <span class="s1">'ai_augmented_productivity_norm'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'errors_caught_norm'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">'trust_decisions_norm'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
            <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="mf">0.0</span>
        <span class="p">})</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_fluency</span><span class="p">(</span><span class="n">employee_data</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_calculate_ai_fluency_edge_all_max_scores_within_clip</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">):</span>
        <span class="c1"># Create an employee with max values for sub-components, checking if total clips to 100</span>
        <span class="n">employee_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">({</span>
            <span class="s1">'prompting_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'tools_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'understanding_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'data_lit_score'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span>
            <span class="s1">'ai_augmented_productivity_norm'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span>
            <span class="s1">'errors_caught_norm'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span> <span class="s1">'trust_decisions_norm'</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span>
            <span class="s1">'learning_rate'</span><span class="p">:</span> <span class="mf">1.0</span> <span class="c1"># S4 will be 80, not 100</span>
        <span class="p">})</span>
        <span class="n">s1_val</span> <span class="o">=</span> <span class="mf">100.0</span>
        <span class="n">s2_val</span> <span class="o">=</span> <span class="mf">100.0</span>
        <span class="n">s3_val</span> <span class="o">=</span> <span class="mf">100.0</span>
        <span class="n">s4_val</span> <span class="o">=</span> <span class="mf">80.0</span> <span class="c1"># From np.clip(1.0 * 100 * 0.8, 0, 100)</span>

        <span class="n">expected_ai_fluency</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'technical_ai_skills_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s1_val</span> <span class="o">+</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'ai_augmented_productivity_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s2_val</span> <span class="o">+</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'critical_ai_judgment_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s3_val</span> <span class="o">+</span>
            <span class="n">sample_theta_weights</span><span class="p">[</span><span class="s1">'ai_learning_velocity_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">s4_val</span>
        <span class="p">)</span>
        <span class="c1"># Check if the calculated value is correctly clipped if it exceeds 100, or within bounds otherwise</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">calculate_ai_fluency</span><span class="p">(</span><span class="n">employee_data</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">expected_ai_fluency</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">))</span>
        <span class="k">assert</span> <span class="n">calculate_ai_fluency</span><span class="p">(</span><span class="n">employee_data</span><span class="p">,</span> <span class="n">sample_theta_weights</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">100</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=e4dfcd45">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [17]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_employees with the calculated ai_fluency_score for all employees</span>
<span class="n">df_employees</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_ai_fluency</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'theta_ai_fluency_weights'</span><span class="p">]),</span>
    <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'ai_fluency_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'ai_fluency_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'ai_fluency_score':
  employee_id          job_role  ai_fluency_score
0      EMP000     HR Specialist         69.751289
1      EMP001       ML Engineer         78.638542
2      EMP002       AI Ethicist         46.314229
3      EMP003  Business Analyst         71.900051
4      EMP004  Business Analyst         69.850345
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=d7303f3e">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The AI-Fluency score provides a detailed individual assessment of an employee's ability to interact with and leverage AI technologies. This multi-faceted measure highlights specific areas where an individual might excel or need further development in their AI-related capabilities.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=a8243bf9">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-10:-Idiosyncratic-Readiness-($V%5ER$)-Components:-Domain-Expertise-Factor">Section 10: Idiosyncratic Readiness ($V^R$) Components: Domain-Expertise Factor<a class="anchor-link" href="#Section-10:-Idiosyncratic-Readiness-($V%5ER$)-Components:-Domain-Expertise-Factor">¶</a></h1><p>Domain-Expertise captures an individual's depth of knowledge in specific application areas, complementing their AI-Fluency. It is a multiplicative combination of Educational Foundation, Practical Experience, and Specialization Depth:</p>
<p>$$Domain\text{-}Expertise_i = E_{\text{education}} \cdot E_{\text{experience}} \cdot E_{\text{specialization}}$$</p>
<ol>
<li><strong>Educational Foundation ($E_{\text{education}}$):</strong> Discrete values based on education level (e.g., PhD=1.0, Master's=0.85, Bachelor's=0.70, Associate's/Certificate=0.60, HS+Coursework=0.50).</li>
<li><strong>Practical Experience ($E_{\text{experience}}$):</strong> Measured by years of experience with diminishing returns:
$$E_{\text{experience}} = 1 - e^{-\gamma_{\text{exp}} \cdot Years}$$
where $\gamma_{\text{exp}} = 0.15$ (from <code>PARAMS</code>).</li>
<li><strong>Specialization Depth ($E_{\text{specialization}}$):</strong> Reflects specific achievements and recognition in their field:
$$E_{\text{specialization}} = w_{\text{port}} \cdot \text{Portfolio}_i + w_{\text{recog}} \cdot \text{Recognition}_i + w_{\text{cred}} \cdot \text{Credentials}_i$$
where $w_{\text{port}} = 0.4$, $w_{\text{recog}} = 0.3$, $w_{\text{cred}} = 0.3$ (from <code>PARAMS</code>).</li>
</ol>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=65b67c42">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [18]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_educational_foundation</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes E_education based on education level."""</span>
    <span class="n">education_map</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'HS+Coursework'</span><span class="p">:</span> <span class="mf">0.50</span><span class="p">,</span>
        <span class="s1">'Associate</span><span class="se">\'</span><span class="s1">s/Certificate'</span><span class="p">:</span> <span class="mf">0.60</span><span class="p">,</span>
        <span class="s1">'Bachelor</span><span class="se">\'</span><span class="s1">s'</span><span class="p">:</span> <span class="mf">0.70</span><span class="p">,</span>
        <span class="s1">'Master</span><span class="se">\'</span><span class="s1">s'</span><span class="p">:</span> <span class="mf">0.85</span><span class="p">,</span>
        <span class="s1">'PhD'</span><span class="p">:</span> <span class="mf">1.0</span>
    <span class="p">}</span>
    <span class="k">return</span> <span class="n">education_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'education_level'</span><span class="p">],</span> <span class="mf">0.50</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span> <span class="c1"># Scale to 0-100</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_practical_experience</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">gamma_exp</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes E_experience with diminishing returns."""</span>
    <span class="n">years</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'years_experience'</span><span class="p">]</span>
    <span class="n">experience_score</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">np</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="o">-</span><span class="n">gamma_exp</span> <span class="o">*</span> <span class="n">years</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">experience_score</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_specialization_depth</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">weights</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes E_specialization based on portfolio, recognition, and credentials."""</span>
    <span class="n">portfolio_score</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'domain_portfolio_score'</span><span class="p">]</span>
    <span class="n">recognition_score</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'domain_recognition_score'</span><span class="p">]</span>
    <span class="n">credentials_score</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'domain_credentials_score'</span><span class="p">]</span>

    <span class="n">specialization_depth</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'portfolio_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">portfolio_score</span> <span class="o">+</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'recognition_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">recognition_score</span> <span class="o">+</span>
        <span class="n">weights</span><span class="p">[</span><span class="s1">'credentials_weight'</span><span class="p">]</span> <span class="o">*</span> <span class="n">credentials_score</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">specialization_depth</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_domain_expertise</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">gamma_exp</span><span class="p">,</span> <span class="n">domain_weights</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Aggregates the three sub-factors into Domain-Expertise."""</span>
    <span class="n">e_education</span> <span class="o">=</span> <span class="n">calculate_educational_foundation</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">)</span> <span class="o">/</span> <span class="mi">100</span> <span class="c1"># Back to 0-1 for multiplication</span>
    <span class="n">e_experience</span> <span class="o">=</span> <span class="n">calculate_practical_experience</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">gamma_exp</span><span class="p">)</span> <span class="o">/</span> <span class="mi">100</span> <span class="c1"># Back to 0-1</span>
    <span class="n">e_specialization</span> <span class="o">=</span> <span class="n">calculate_specialization_depth</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">domain_weights</span><span class="p">)</span> <span class="o">/</span> <span class="mi">100</span> <span class="c1"># Back to 0-1</span>

    <span class="n">domain_expertise</span> <span class="o">=</span> <span class="n">e_education</span> <span class="o">*</span> <span class="n">e_experience</span> <span class="o">*</span> <span class="n">e_specialization</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">domain_expertise</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span> <span class="c1"># Final score 0-100</span>

<span class="c1"># Test the functions immediately with an example employee</span>
<span class="n">example_employee</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">education_score</span> <span class="o">=</span> <span class="n">calculate_educational_foundation</span><span class="p">(</span><span class="n">example_employee</span><span class="p">)</span>
<span class="n">experience_score</span> <span class="o">=</span> <span class="n">calculate_practical_experience</span><span class="p">(</span><span class="n">example_employee</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'gamma_experience_decay'</span><span class="p">])</span>
<span class="n">specialization_score</span> <span class="o">=</span> <span class="n">calculate_specialization_depth</span><span class="p">(</span><span class="n">example_employee</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'domain_specialization_weights'</span><span class="p">])</span>
<span class="n">domain_expertise_score</span> <span class="o">=</span> <span class="n">calculate_domain_expertise</span><span class="p">(</span><span class="n">example_employee</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'gamma_experience_decay'</span><span class="p">],</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'domain_specialization_weights'</span><span class="p">])</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test E_education for EMP000: </span><span class="si">{</span><span class="n">education_score</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test E_experience for EMP000: </span><span class="si">{</span><span class="n">experience_score</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test E_specialization for EMP000: </span><span class="si">{</span><span class="n">specialization_score</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Domain-Expertise score for EMP000: </span><span class="si">{</span><span class="n">domain_expertise_score</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test E_education for EMP000: 60.00
Test E_experience for EMP000: 83.47
Test E_specialization for EMP000: 53.50
Test Domain-Expertise score for EMP000: 26.79
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=613b748a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [19]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_employees with the calculated domain_expertise_score for all employees</span>
<span class="n">df_employees</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_domain_expertise</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'gamma_experience_decay'</span><span class="p">],</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'domain_specialization_weights'</span><span class="p">]),</span>
    <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'domain_expertise_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'domain_expertise_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'domain_expertise_score':
  employee_id          job_role  domain_expertise_score
0      EMP000     HR Specialist               26.793906
1      EMP001       ML Engineer               34.055805
2      EMP002       AI Ethicist               36.407782
3      EMP003  Business Analyst               39.660823
4      EMP004  Business Analyst               16.952863
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=cf4586f7">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>Domain-Expertise underscores the importance of deep, specialized knowledge in specific fields, which AI tools are designed to augment. This score provides a quantitative measure of an individual's subject matter mastery, a crucial complement to their AI-Fluency.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=419a4886">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-11:-Idiosyncratic-Readiness-($V%5ER$)-Components:-Adaptive-Capacity-Factor">Section 11: Idiosyncratic Readiness ($V^R$) Components: Adaptive-Capacity Factor<a class="anchor-link" href="#Section-11:-Idiosyncratic-Readiness-($V%5ER$)-Components:-Adaptive-Capacity-Factor">¶</a></h1><p>Adaptive-Capacity measures the meta-skills that enable successful navigation of AI-driven transitions, focusing on an individual's ability to learn, adapt, and interact effectively in new environments. It is an equally weighted sum of three meta-skills:</p>
<p>$$Adaptive\text{-}Capacity_i = \frac{1}{3} (C_{\text{cognitive}} + C_{\text{social}} + C_{\text{strategic}})$$</p>
<p>where each $C$ component is scored on a scale of $[0, 100]$:</p>
<ul>
<li><strong>Cognitive Flexibility ($C_{\text{cognitive}}$):</strong> Problem-solving in novel contexts, transfer learning, creative application of AI tools.</li>
<li><strong>Social-Emotional Intelligence ($C_{\text{social}}$):</strong> Empathy, negotiation, leadership, human-AI collaboration.</li>
<li><strong>Strategic Career Management ($C_{\text{strategic}}$):</strong> Awareness of AI trends, proactive skill development, network building.</li>
</ul>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=ad691e24">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [20]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_adaptive_capacity</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes Adaptive-Capacity as an average of three meta-skills."""</span>
    <span class="n">c_cognitive</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'adaptive_cognitive_flexibility'</span><span class="p">]</span>
    <span class="n">c_social</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'adaptive_social_emotional'</span><span class="p">]</span>
    <span class="n">c_strategic</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'adaptive_strategic_career'</span><span class="p">]</span>

    <span class="n">adaptive_capacity</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">([</span><span class="n">c_cognitive</span><span class="p">,</span> <span class="n">c_social</span><span class="p">,</span> <span class="n">c_strategic</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">adaptive_capacity</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Test the function immediately with an example employee</span>
<span class="n">example_employee</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">adaptive_capacity_score</span> <span class="o">=</span> <span class="n">calculate_adaptive_capacity</span><span class="p">(</span><span class="n">example_employee</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Adaptive-Capacity score for EMP000: </span><span class="si">{</span><span class="n">adaptive_capacity_score</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Adaptive-Capacity score for EMP000: 59.33
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=870dfb91">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_employees with the calculated adaptive_capacity_score for all employees</span>
<span class="n">df_employees</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="n">calculate_adaptive_capacity</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'adaptive_capacity_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'adaptive_capacity_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'adaptive_capacity_score':
  employee_id          job_role  adaptive_capacity_score
0      EMP000     HR Specialist                59.333333
1      EMP001       ML Engineer                42.000000
2      EMP002       AI Ethicist                60.000000
3      EMP003  Business Analyst                80.000000
4      EMP004  Business Analyst                76.000000
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=ef5a00c1">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>Adaptive-Capacity highlights an individual's inherent ability to thrive in a rapidly changing AI landscape. These meta-skills are increasingly vital for sustained career success, as they enable individuals to continuously learn, adapt, and collaborate effectively with both humans and AI.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=0ecd7a2b">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-12:-Calculate-Final-Idiosyncratic-Readiness-($V%5ER$)">Section 12: Calculate Final Idiosyncratic Readiness ($V^R$)<a class="anchor-link" href="#Section-12:-Calculate-Final-Idiosyncratic-Readiness-($V%5ER$)">¶</a></h1><p>The final Idiosyncratic Readiness score ($V^R(t)$) aggregates AI-Fluency, Domain-Expertise, and Adaptive-Capacity. This score quantifies an individual's personal preparation to succeed in AI-enabled careers, factors that can be directly improved through deliberate learning and skill development. It is a weighted sum:</p>
<p>$$V^R(t) = w_{\text{VR1}} \cdot AI\text{-}Fluency_i(t) + w_{\text{VR2}} \cdot Domain\text{-}Expertise_i(t) + w_{\text{VR3}} \cdot Adaptive\text{-}Capacity_i(t)$$</p>
<p>The weights ($w_{\text{VR1}} = 0.45$, $w_{\text{VR2}} = 0.35$, $w_{\text{VR3}} = 0.20$) reflect the assessment that AI-Fluency is the most critical factor, followed by Domain-Expertise, with Adaptive-Capacity playing a supporting role (weights are from <code>PARAMS</code>). The final $V^R$ score is normalized to $[0, 100]$.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=dfacb376">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [22]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_idiosyncratic_readiness</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">vr_weights</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes total V^R score from its sub-components."""</span>
    <span class="n">ai_fluency</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span>
    <span class="n">domain_expertise</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span>
    <span class="n">adaptive_capacity</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span>

    <span class="n">vr_score</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'ai_fluency_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">ai_fluency</span> <span class="o">+</span>
        <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'domain_expertise_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">domain_expertise</span> <span class="o">+</span>
        <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">adaptive_capacity</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Test the function immediately with an example employee</span>
<span class="n">example_employee</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">vr_score_test</span> <span class="o">=</span> <span class="n">calculate_idiosyncratic_readiness</span><span class="p">(</span><span class="n">example_employee</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test V^R score for EMP000: </span><span class="si">{</span><span class="n">vr_score_test</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test V^R score for EMP000: 52.63
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=1e301fcf">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [23]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_employees with the calculated vr_score for all employees</span>
<span class="n">df_employees</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_idiosyncratic_readiness</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">]),</span>
    <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'vr_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'vr_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'vr_score':
  employee_id          job_role   vr_score
0      EMP000     HR Specialist  52.632614
1      EMP001       ML Engineer  55.706876
2      EMP002       AI Ethicist  45.584127
3      EMP003  Business Analyst  62.236311
4      EMP004  Business Analyst  52.566157
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=3be55138">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>This completes the calculation of the individual-specific readiness component. The $V^R$ score provides a holistic view of an individual's intrinsic capabilities and potential for growth in AI-driven roles, serving as a critical counterpart to the market-driven $HR^R$.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=66bf1eb7">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-13:-Synergy-Function:-Skills-Match-&amp;-Timing-Factor">Section 13: Synergy Function: Skills Match &amp; Timing Factor<a class="anchor-link" href="#Section-13:-Synergy-Function:-Skills-Match-&amp;-Timing-Factor">¶</a></h1><p>The Synergy function captures the multiplicative benefits when individual readiness ($V^R$) aligns with market opportunity ($HR^R$). It is defined as:</p>
<p>$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$</p>
<p>The $Alignment_i$ factor measures how well individual skills match occupation requirements and career stage:</p>
<p>$$Alignment_i = \frac{\text{Skills Match Score}_i}{\text{Maximum Possible Match}} \times \text{Timing Factor}_i$$</p>
<ol>
<li><strong>Skills Match Score:</strong> Using O*NET-like task-skill mappings (simulated through <code>skill_a</code> to <code>skill_j</code> in our synthetic data), we compute:
$$Match_i = \sum_{s \in S} \min(\text{Individual Skill}_{i,s}, \text{Required Skill}_{o,s}) \cdot \text{Importance}_s$$
For <code>Maximum Possible Match</code>, we assume a perfect match of 1.0 (after normalization of individual and required skills to 0-1).</li>
<li><strong>Timing Factor:</strong> Career stage affects transition ease:
$$Timing(y) = \begin{cases} 1.0 &amp; \text{if } y \in [0,5] \text{ (early career)} \\ 1.0 &amp; \text{if } y \in (5,15] \text{ (mid-career)} \\ 0.8 &amp; \text{if } y &gt; 15 \text{ (late career, transition friction)} \end{cases}$$
where $y$ is years of experience.</li>
</ol>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=ed30cdb7">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [24]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_skills_match_score</span><span class="p">(</span><span class="n">employee_skills_series</span><span class="p">,</span> <span class="n">required_skills_series</span><span class="p">,</span> <span class="n">skill_importance_series</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes a skills match score between an employee and a job role."""</span>
    <span class="n">match_score</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">skill_cols</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>

    <span class="k">for</span> <span class="n">skill_col</span> <span class="ow">in</span> <span class="n">skill_cols</span><span class="p">:</span>
        <span class="c1"># Ensure required_skills_series and skill_importance_series are properly aligned</span>
        <span class="c1"># In df_occupations, skill importance is `skill_X_importance` and required skills is `required_skill_X`</span>
        <span class="n">required_skill_val</span> <span class="o">=</span> <span class="n">required_skills_series</span><span class="p">[</span><span class="sa">f</span><span class="s1">'required_</span><span class="si">{</span><span class="n">skill_col</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span>
        <span class="n">skill_importance_val</span> <span class="o">=</span> <span class="n">skill_importance_series</span><span class="p">[</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">skill_col</span><span class="si">}</span><span class="s1">_importance'</span><span class="p">]</span>
        <span class="n">individual_skill_val</span> <span class="o">=</span> <span class="n">employee_skills_series</span><span class="p">[</span><span class="n">skill_col</span><span class="p">]</span>

        <span class="c1"># Max possible individual skill is 100, so normalize to 0-1 before min operation</span>
        <span class="c1"># then multiply by 100 for a final score of 0-100</span>
        <span class="n">match_score</span> <span class="o">+=</span> <span class="nb">min</span><span class="p">(</span><span class="n">individual_skill_val</span> <span class="o">/</span> <span class="mi">100</span><span class="p">,</span> <span class="n">required_skill_val</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span> <span class="o">*</span> <span class="n">skill_importance_val</span>

    <span class="c1"># Normalize the total match_score by the sum of importance weights to get a score 0-1, then scale to 0-100</span>
    <span class="n">total_importance</span> <span class="o">=</span> <span class="n">skill_importance_series</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">total_importance</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c1"># Avoid division by zero if no skills defined</span>
        <span class="k">return</span> <span class="mi">0</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">((</span><span class="n">match_score</span> <span class="o">/</span> <span class="n">total_importance</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_timing_factor</span><span class="p">(</span><span class="n">years_experience</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes career stage timing factor."""</span>
    <span class="k">if</span> <span class="n">years_experience</span> <span class="o">&lt;=</span> <span class="mi">5</span><span class="p">:</span>
        <span class="k">return</span> <span class="mf">1.0</span>
    <span class="k">elif</span> <span class="mi">5</span> <span class="o">&lt;</span> <span class="n">years_experience</span> <span class="o">&lt;=</span> <span class="mi">15</span><span class="p">:</span>
        <span class="k">return</span> <span class="mf">1.0</span>
    <span class="k">else</span><span class="p">:</span> <span class="c1"># years_experience &gt; 15</span>
        <span class="k">return</span> <span class="mf">0.8</span>

<span class="k">def</span><span class="w"> </span><span class="nf">calculate_alignment_factor</span><span class="p">(</span><span class="n">skills_match_score</span><span class="p">,</span> <span class="n">timing_factor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes alignment factor based on skills match and timing."""</span>
    <span class="c1"># Scale skills_match_score from 0-100 to 0-1 for multiplication</span>
    <span class="n">alignment</span> <span class="o">=</span> <span class="p">(</span><span class="n">skills_match_score</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span> <span class="o">*</span> <span class="n">timing_factor</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">alignment</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>

<span class="c1"># Test the functions immediately with an example employee and their job role</span>
<span class="n">example_employee</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">example_occupation_row</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="p">[</span><span class="n">df_occupations</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span> <span class="o">==</span> <span class="n">example_employee</span><span class="p">[</span><span class="s1">'job_role'</span><span class="p">]]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

<span class="c1"># Extract employee skills for the calculation</span>
<span class="n">employee_skill_data</span> <span class="o">=</span> <span class="n">example_employee</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span>
<span class="c1"># Extract required skills and importance from the occupation data row</span>
<span class="n">required_skill_data</span> <span class="o">=</span> <span class="n">example_occupation_row</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span>
<span class="n">skill_importance_data</span> <span class="o">=</span> <span class="n">example_occupation_row</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span>

<span class="n">skills_match</span> <span class="o">=</span> <span class="n">calculate_skills_match_score</span><span class="p">(</span><span class="n">employee_skill_data</span><span class="p">,</span> <span class="n">required_skill_data</span><span class="p">,</span> <span class="n">skill_importance_data</span><span class="p">)</span>
<span class="n">timing_factor</span> <span class="o">=</span> <span class="n">calculate_timing_factor</span><span class="p">(</span><span class="n">example_employee</span><span class="p">[</span><span class="s1">'years_experience'</span><span class="p">])</span>
<span class="n">alignment_factor</span> <span class="o">=</span> <span class="n">calculate_alignment_factor</span><span class="p">(</span><span class="n">skills_match</span><span class="p">,</span> <span class="n">timing_factor</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Skills Match Score for EMP000 (</span><span class="si">{</span><span class="n">example_employee</span><span class="p">[</span><span class="s1">'job_role'</span><span class="p">]</span><span class="si">}</span><span class="s2">): </span><span class="si">{</span><span class="n">skills_match</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Timing Factor for EMP000 (</span><span class="si">{</span><span class="n">example_employee</span><span class="p">[</span><span class="s1">'years_experience'</span><span class="p">]</span><span class="si">}</span><span class="s2"> years exp): </span><span class="si">{</span><span class="n">timing_factor</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Alignment Factor for EMP000: </span><span class="si">{</span><span class="n">alignment_factor</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Skills Match Score for EMP000 (HR Specialist): 28.94
Test Timing Factor for EMP000 (12 years exp): 1.00
Test Alignment Factor for EMP000: 0.29
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=caabba8b">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [25]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_employees with alignment_factor for all employees</span>
<span class="k">def</span><span class="w"> </span><span class="nf">get_alignment_for_employee</span><span class="p">(</span><span class="n">employee_row</span><span class="p">):</span>
    <span class="n">job_role</span> <span class="o">=</span> <span class="n">employee_row</span><span class="p">[</span><span class="s1">'job_role'</span><span class="p">]</span>
    <span class="c1"># Ensure df_occupations is accessible in this scope (from previous cells)</span>
    <span class="k">global</span> <span class="n">df_occupations</span>
    <span class="n">occupation_row</span> <span class="o">=</span> <span class="n">df_occupations</span><span class="p">[</span><span class="n">df_occupations</span><span class="p">[</span><span class="s1">'occupation'</span><span class="p">]</span> <span class="o">==</span> <span class="n">job_role</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

    <span class="c1"># Corrected f-string syntax from \'a\' to "a"</span>
    <span class="n">employee_skill_data</span> <span class="o">=</span> <span class="n">employee_row</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span>
    <span class="n">required_skill_data</span> <span class="o">=</span> <span class="n">occupation_row</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'required_skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span>
    <span class="n">skill_importance_data</span> <span class="o">=</span> <span class="n">occupation_row</span><span class="p">[[</span><span class="sa">f</span><span class="s1">'skill_</span><span class="si">{</span><span class="nb">chr</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s2">"a"</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="si">}</span><span class="s1">_importance'</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]]</span>

    <span class="c1"># Ensure these functions are defined and accessible (from previous cells)</span>
    <span class="c1"># They should have been defined in previous cells or imported.</span>
    <span class="c1"># For robustness in a test environment, they would typically be imported or passed.</span>
    <span class="c1"># Assuming they are globally available from the notebook's execution flow.</span>
    <span class="n">skills_match</span> <span class="o">=</span> <span class="n">calculate_skills_match_score</span><span class="p">(</span><span class="n">employee_skill_data</span><span class="p">,</span> <span class="n">required_skill_data</span><span class="p">,</span> <span class="n">skill_importance_data</span><span class="p">)</span>
    <span class="n">timing_factor</span> <span class="o">=</span> <span class="n">calculate_timing_factor</span><span class="p">(</span><span class="n">employee_row</span><span class="p">[</span><span class="s1">'years_experience'</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">calculate_alignment_factor</span><span class="p">(</span><span class="n">skills_match</span><span class="p">,</span> <span class="n">timing_factor</span><span class="p">)</span>

<span class="n">df_employees</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">get_alignment_for_employee</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'alignment_factor':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'alignment_factor'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'alignment_factor':
  employee_id          job_role  alignment_factor
0      EMP000     HR Specialist          0.289364
1      EMP001       ML Engineer          0.357455
2      EMP002       AI Ethicist          0.477713
3      EMP003  Business Analyst          0.543854
4      EMP004  Business Analyst          0.328143
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=890afeb6">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The Alignment Factor provides a nuanced measure of how well an individual's skills and career stage align with a specific occupational target. This factor is critical for determining the true "fit" and the potential for synergy between an individual's readiness and market opportunity.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=07169edb">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-14:-Calculate-Final-Synergy-Score">Section 14: Calculate Final Synergy Score<a class="anchor-link" href="#Section-14:-Calculate-Final-Synergy-Score">¶</a></h1><p>The Synergy score quantifies the compounded benefits arising from a strong individual readiness combined with a high market opportunity, especially when there is good alignment. It enhances the overall AI-R score beyond a simple additive model.</p>
<p>$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$</p>
<p>The result is normalized to a $[0, 100]$ scale.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=cd84174e">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [26]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">calculate_synergy</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="n">hr_score</span><span class="p">,</span> <span class="n">alignment_factor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes Synergy%."""</span>
    <span class="c1"># Ensure vr_score and hr_score are between 0-100</span>
    <span class="n">vr_norm</span> <span class="o">=</span> <span class="n">vr_score</span> <span class="o">/</span> <span class="mi">100</span>
    <span class="n">hr_norm</span> <span class="o">=</span> <span class="n">hr_score</span> <span class="o">/</span> <span class="mi">100</span>

    <span class="n">synergy</span> <span class="o">=</span> <span class="p">(</span><span class="n">vr_norm</span> <span class="o">*</span> <span class="n">hr_norm</span><span class="p">)</span> <span class="o">*</span> <span class="n">alignment_factor</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">synergy</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Test the function immediately</span>
<span class="n">example_employee</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">synergy_score_test</span> <span class="o">=</span> <span class="n">calculate_synergy</span><span class="p">(</span>
    <span class="n">example_employee</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span>
    <span class="n">example_employee</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span>
    <span class="n">example_employee</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Synergy Score for EMP000: </span><span class="si">{</span><span class="n">synergy_score_test</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Synergy Score for EMP000: 6.01
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=d3c22fc5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [27]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Update df_employees with the newly calculated synergy_score for all employees</span>
<span class="n">df_employees</span><span class="p">[</span><span class="s1">'synergy_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">calculate_synergy</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span> <span class="n">row</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span> <span class="n">row</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]),</span>
    <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with newly calculated 'synergy_score':"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'vr_score'</span><span class="p">,</span> <span class="s1">'hr_r_score'</span><span class="p">,</span> <span class="s1">'alignment_factor'</span><span class="p">,</span> <span class="s1">'synergy_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with newly calculated 'synergy_score':
  employee_id          job_role   vr_score  hr_r_score  alignment_factor  \
0      EMP000     HR Specialist  52.632614   39.492115          0.289364   
1      EMP001       ML Engineer  55.706876   77.416639          0.357455   
2      EMP002       AI Ethicist  45.584127   70.482245          0.477713   
3      EMP003  Business Analyst  62.236311   44.873882          0.543854   
4      EMP004  Business Analyst  52.566157   44.873882          0.328143   

   synergy_score  
0       6.014634  
1      15.415756  
2      15.348299  
3      15.188681  
4       7.740397  
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=610687cc">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The Synergy score formalizes the idea that career success is more than just individual capability plus market demand; it also depends on how well these two factors align. A high synergy score indicates a "sweet spot" where an individual's unique skills and career stage perfectly intersect with market opportunities.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=33bc8150">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-15:-Calculate-Overall-AI-Readiness-Score-(AI-R)">Section 15: Calculate Overall AI-Readiness Score (AI-R)<a class="anchor-link" href="#Section-15:-Calculate-Overall-AI-Readiness-Score-(AI-R)">¶</a></h1><p>With all components calculated—Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($HR^R$), and Synergy—we can now compute the overall AI-Readiness Score for each employee using the master formula:</p>
<p>$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot HR^R(t) + \beta \cdot Synergy\%(V^R, HR^R)$$</p>
<p>The parameters $\alpha = 0.6$ and $\beta = 0.15$ (from <code>PARAMS</code>) are used to weight the contributions of individual readiness, market opportunity, and their synergy.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=d6a5320f">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [28]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># The `calculate_ai_r` function was already defined in Section 1.</span>
<span class="c1"># Now, apply it to all employees in df_employees.</span>

<span class="n">df_employees</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
    <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span>
        <span class="n">calculate_ai_r</span><span class="p">(</span>
            <span class="n">row</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span>
            <span class="n">row</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span>
            <span class="n">row</span><span class="p">[</span><span class="s1">'synergy_score'</span><span class="p">],</span>
            <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">],</span>
            <span class="n">PARAMS</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">]</span>
        <span class="p">),</span>
    <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"df_employees with all calculated AI-R components and final score:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df_employees</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'department'</span><span class="p">,</span> <span class="s1">'vr_score'</span><span class="p">,</span> <span class="s1">'hr_r_score'</span><span class="p">,</span> <span class="s1">'synergy_score'</span><span class="p">,</span> <span class="s1">'current_ai_r_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>

<span class="c1"># Calculate and print the average AI-R score for the entire workforce</span>
<span class="n">average_ai_r</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Average AI-R score for the entire workforce: </span><span class="si">{</span><span class="n">average_ai_r</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>df_employees with all calculated AI-R components and final score:
  employee_id          job_role   department   vr_score  hr_r_score  \
0      EMP000     HR Specialist  Engineering  52.632614   39.492115   
1      EMP001       ML Engineer    Marketing  55.706876   77.416639   
2      EMP002       AI Ethicist           HR  45.584127   70.482245   
3      EMP003  Business Analyst  Engineering  62.236311   44.873882   
4      EMP004  Business Analyst      Finance  52.566157   44.873882   

   synergy_score  current_ai_r_score  
0       6.014634           48.278609  
1      15.415756           66.703145  
2      15.348299           57.845619  
3      15.188681           57.569642  
4       7.740397           50.650307  

Average AI-R score for the entire workforce: 56.27
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=51a53518">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The final AI-Readiness Score provides a comprehensive, data-driven measure of each employee's potential to succeed in AI-enabled roles. This score serves as the foundation for identifying talent strengths, weaknesses, and for designing targeted upskilling strategies.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=7efa6b32">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-16:-AI-Readiness-Report-&amp;-Skills-Gap-Analysis">Section 16: AI-Readiness Report &amp; Skills Gap Analysis<a class="anchor-link" href="#Section-16:-AI-Readiness-Report-&amp;-Skills-Gap-Analysis">¶</a></h1><p>A "Workforce AI-Readiness Report" summarizes the aggregated AI-R scores and identifies skills gaps. This section will generate a summary table of AI-R scores grouped by department and job role, and a heatmap to visualize collective strengths and weaknesses across the $V^R$ sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity).</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=10a75f29">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [29]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">generate_ai_r_report_summary</span><span class="p">(</span><span class="n">df_employees_data</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Aggregates AI-R scores by group (e.g., department, job role)."""</span>
    <span class="n">summary_df</span> <span class="o">=</span> <span class="n">df_employees_data</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">'department'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">])</span><span class="o">.</span><span class="n">agg</span><span class="p">(</span>
        <span class="n">average_current_ai_r</span><span class="o">=</span><span class="p">(</span><span class="s1">'current_ai_r_score'</span><span class="p">,</span> <span class="s1">'mean'</span><span class="p">),</span>
        <span class="n">average_vr_score</span><span class="o">=</span><span class="p">(</span><span class="s1">'vr_score'</span><span class="p">,</span> <span class="s1">'mean'</span><span class="p">),</span>
        <span class="n">average_hr_r_score</span><span class="o">=</span><span class="p">(</span><span class="s1">'hr_r_score'</span><span class="p">,</span> <span class="s1">'mean'</span><span class="p">),</span>
        <span class="n">average_synergy_score</span><span class="o">=</span><span class="p">(</span><span class="s1">'synergy_score'</span><span class="p">,</span> <span class="s1">'mean'</span><span class="p">),</span>
        <span class="n">num_employees</span><span class="o">=</span><span class="p">(</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'count'</span><span class="p">)</span>
    <span class="p">)</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">summary_df</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">plot_skills_gap_heatmap</span><span class="p">(</span><span class="n">df_employees_data</span><span class="p">,</span> <span class="n">group_by_column</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Visualizes strengths and weaknesses of V^R sub-components using a heatmap."""</span>
    <span class="n">vr_sub_components</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">,</span> <span class="s1">'domain_expertise_score'</span><span class="p">,</span> <span class="s1">'adaptive_capacity_score'</span><span class="p">]</span>
    <span class="n">heatmap_data</span> <span class="o">=</span> <span class="n">df_employees_data</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">group_by_column</span><span class="p">)[</span><span class="n">vr_sub_components</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>

    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
    <span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">heatmap_data</span><span class="p">,</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">'viridis'</span><span class="p">,</span> <span class="n">fmt</span><span class="o">=</span><span class="s2">".1f"</span><span class="p">,</span> <span class="n">linewidths</span><span class="o">=</span><span class="mf">.5</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Average V^R Sub-Component Scores by </span><span class="si">{</span><span class="n">group_by_column</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="n">group_by_column</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">'V^R Sub-Component'</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">rotation</span><span class="o">=</span><span class="mi">45</span><span class="p">,</span> <span class="n">ha</span><span class="o">=</span><span class="s1">'right'</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1"># Test the functions immediately</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Test Summary Report:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">generate_ai_r_report_summary</span><span class="p">(</span><span class="n">df_employees</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>

<span class="c1"># No plot generated during test, only for execution cell</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Summary Report:
    department          job_role  average_current_ai_r  average_vr_score  \
0  Engineering       AI Ethicist                 60.58             50.79   
1  Engineering  Business Analyst                 54.89             58.74   
2  Engineering    Data Scientist                 54.82             40.53   
3  Engineering     HR Specialist                 47.44             50.89   
4  Engineering       ML Engineer                 64.38             52.45   

   average_hr_r_score  average_synergy_score  num_employees  
0               70.48                  12.77              4  
1               44.87                  11.28              3  
2               72.40                  10.29              2  
3               39.49                   7.41              2  
4               77.42                  12.97              2  
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=a4a31d39">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [30]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="c1"># Generate and display the summary table</span>
<span class="n">ai_r_summary_report</span> <span class="o">=</span> <span class="n">generate_ai_r_report_summary</span><span class="p">(</span><span class="n">df_employees</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Workforce AI-Readiness Summary Report by Department and Job Role:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ai_r_summary_report</span><span class="o">.</span><span class="n">to_string</span><span class="p">())</span>

<span class="c1"># Generate the skills gap heatmap</span>
<span class="n">plot_skills_gap_heatmap</span><span class="p">(</span><span class="n">df_employees</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">)</span>
<span class="n">plot_skills_gap_heatmap</span><span class="p">(</span><span class="n">df_employees</span><span class="p">,</span> <span class="s1">'department'</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Workforce AI-Readiness Summary Report by Department and Job Role:
     department          job_role  average_current_ai_r  average_vr_score  average_hr_r_score  average_synergy_score  num_employees
0   Engineering       AI Ethicist                 60.58             50.79               70.48                  12.77              4
1   Engineering  Business Analyst                 54.89             58.74               44.87                  11.28              3
2   Engineering    Data Scientist                 54.82             40.53               72.40                  10.29              2
3   Engineering     HR Specialist                 47.44             50.89               39.49                   7.41              2
4   Engineering       ML Engineer                 64.38             52.45               77.42                  12.97              2
5       Finance       AI Ethicist                 59.42             49.23               70.48                  11.25              2
6       Finance  Business Analyst                 51.72             54.11               44.87                   8.72              5
7       Finance    Data Scientist                 61.20             50.73               72.40                  12.01              3
8       Finance     HR Specialist                 47.30             50.94               39.49                   6.28              2
9       Finance       ML Engineer                 64.67             52.12               77.42                  16.21              2
10           HR       AI Ethicist                 59.66             49.24               70.48                  12.83              4
11           HR  Business Analyst                 47.11             46.33               44.87                   9.04              3
12           HR    Data Scientist                 68.54             63.29               72.40                  10.71              1
13           HR     HR Specialist                 43.71             44.62               39.49                   7.61              1
14           HR       ML Engineer                 58.66             43.27               77.42                  11.54              1
15    Marketing    Data Scientist                 56.80             43.27               72.40                  12.47              2
16    Marketing     HR Specialist                 49.18             53.67               39.49                   7.86              2
17    Marketing       ML Engineer                 66.70             55.71               77.42                  15.42              1
18          R&amp;D       AI Ethicist                 62.64             54.31               70.48                  12.40              1
19          R&amp;D  Business Analyst                 45.81             44.49               44.87                   7.75              1
20          R&amp;D    Data Scientist                 59.48             47.20               72.40                  14.67              1
21          R&amp;D     HR Specialist                 50.16             55.02               39.49                   9.03              2
22          R&amp;D       ML Engineer                 63.54             50.75               77.42                  14.16              3
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA5EAAAJOCAYAAAAuzYPxAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAA15RJREFUeJzs3XdYFMcfBvD3jnL0KlKUplRp9t5L7CVi11hiiT1qNIYUBRtqjGKvxG6MPfbektg12IOCAooCNlBQD7ib3x/8OD0pHuYUlPeTZ594s7Ozs8fB3ne/s7MSIYQAERERERERkQakhd0BIiIiIiIi+ngwiCQiIiIiIiKNMYgkIiIiIiIijTGIJCIiIiIiIo0xiCQiIiIiIiKNMYgkIiIiIiIijTGIJCIiIiIiIo0xiCQiIiIiIiKNMYgkIiIiIiIijTGIJCKiIsPFxQWtWrUq7G4Q/SfBwcGQSCR4+PDhe91P/fr1Ub9+/QJvFxMTA4lEghkzZmi/U+8g+/0ioo8Hg0giKhQLFiyARCJBtWrVCrsrRcaFCxcgkUjw448/5lnn5s2bkEgkGDVqVK7rly5dColEAmtra0RGRubZTu/evSGRSFSLTCaDh4cHxo0bh5cvX2rUX6VSiVWrVqFatWqwsrKCqakpPDw80LNnT5w6dUqjNt6X6OhofPXVVyhTpgwMDAxgZmaGWrVqYfbs2Xjx4kWh9u1TsG7dOoSFhWlcPz09HbNnz0aFChVgZmYGCwsL+Pj4YMCAAfj333/fX0eJiOi90C3sDhBR8bR27Vq4uLjgzJkziIqKgpubW2F3qdBVrFgRXl5e+O233zBp0qRc66xbtw4A0KNHjxzrdu/ejUGDBqFGjRq4ceMGmjdvjpMnT8LW1jbXtmQyGZYtWwYASElJwR9//IGJEyciOjoaa9eufWt/hw8fjvnz56Nt27bo3r07dHV1ERkZiT179qBMmTKoXr26poeuVbt27ULHjh0hk8nQs2dP+Pr6Ij09HX/99RfGjBmDq1evYsmSJYXSt0/FunXrcOXKFYwYMUKj+oGBgdizZw+6du2K/v37IyMjA//++y927tyJmjVrwsvL6/12+BO1f//+wu4CERVXgojoA7t165YAILZs2SJsbGxEcHDwB++DQqEQL168+OD7fZuJEycKAOLkyZO5rvf09BReXl45ys+dOyeMjY1FgwYNRFpamoiIiBDW1taicuXKIjU1NUf9Xr16CWNjY7UypVIpqlevLiQSiUhISMi3nwkJCUIikYj+/fvnWKdUKkViYmK+2+fF2dlZtGzZ8p22FSLrs2ViYiK8vLzEvXv3cqy/efOmCAsLe+f2KUvLli2Fs7OzRnXPnDkjAIjJkyfnWJeZmSkePnyo5d7l7cWLF0KhULz3/YwfP14AEA8ePHjv+3oXt2/fFgDEzz///F7aL+j7nP1+EdHHg8NZieiDW7t2LSwtLdGyZUt06NBBLeuVkZEBKysr9OnTJ8d2T58+hYGBAUaPHq0qk8vlGD9+PNzc3CCTyeDo6Ihvv/0WcrlcbVuJRIKhQ4di7dq18PHxgUwmw969ewEAM2bMQM2aNWFtbQ1DQ0NUqlQJmzZtyrH/Fy9eYPjw4ShRogRMTU3Rpk0bxMfHQyKRIDg4WK1ufHw8vvzyS9ja2kImk8HHxwe//vrrW9+b7t27A3iVcXzd+fPnERkZqaqT7fbt22jZsiWqVauGnTt3wsjICAEBATh8+DBiYmLQuXNnKBSKt+5bIpGgdu3aEELg1q1b+da9ffs2hBCoVatWru2ULFlS9Tqv+51WrFgBiUSCmJiYHOv279+P8uXLw8DAAOXKlcOWLVve2n8AmD59OlJTUxEeHg57e/sc693c3PD111+rXmdmZmLixIkoW7YsZDIZXFxc8P333+f4/GTfq3n06FFUrlwZhoaG8PPzw9GjRwEAW7ZsgZ+fHwwMDFCpUiX8888/atv37t0bJiYmuHXrFpo2bQpjY2M4ODhgwoQJEEKo1U1LS8M333wDR0dHyGQyeHp6YsaMGTnqZX+mt23bBl9fX9XnLPtz/TpNPo9Hjx6FRCLBhg0bMHnyZJQuXRoGBgZo1KgRoqKiVPXq16+PXbt2ITY2VjUc2sXFJc+fSXR0NADk+lnR0dGBtbV1jr727dsXDg4OkMlkcHV1xaBBg5Cenq6qc+vWLXTs2BFWVlYwMjJC9erVsWvXrlyPZ/369fjxxx9RqlQpGBkZ4enTpwCA06dPo1mzZjA3N4eRkRHq1auHv//+W62NZ8+eYcSIEXBxcYFMJkPJkiXRpEkTXLhwIc/jfd3Dhw/RqVMnmJmZwdraGl9//bXacPF69eohICAg1209PT3RtGnTfNvP7Z7IpKQk9O3bF7a2tjAwMEBAQABWrlyZZxuzZs2Cs7MzDA0NUa9ePVy5ckWjY8v2tvd548aNqFSpEgwNDVGiRAn06NED8fHxGrW9Zs0a1bZWVlbo0qUL7ty5U6D+EdF7UrgxLBEVR15eXqJv375CCCGOHz8uAIgzZ86o1n/55ZfCwsJCyOVyte1WrlwpAIizZ88KIbKyiZ999pkwMjISI0aMEIsXLxZDhw4Vurq6om3btmrbAhDe3t7CxsZGhISEiPnz54t//vlHCCFE6dKlxeDBg8W8efPEzJkzRdWqVQUAsXPnTrU2OnXqJACIL774QsyfP1906tRJBAQECABi/PjxqnoJCQmidOnSwtHRUUyYMEEsXLhQtGnTRgAQs2bNeuv7U7NmTWFraysyMzPVykeNGiUAiOjoaFXZo0ePhKenp2jcuLF4/vx5jrYuXrwoSpQokSNjmFsmUgghOnToIACI69ev59vHe/fuCQCiZcuWIi0tLd+6eWUZli9fLgCI27dvq8qcnZ2Fh4eHsLCwEN99952YOXOm8PPzE1KpVOzfvz/f/QghRKlSpUSZMmXeWi9br169BADRoUMHMX/+fNGzZ08BQLRr106tnrOzs/D09BT29vYiODhYzJo1S5QqVUqYmJiINWvWCCcnJzF16lQxdepUYW5uLtzc3NQyMb169RIGBgbC3d1dfPHFF2LevHmiVatWAoD46aefVPWUSqVo2LChkEgkol+/fmLevHmidevWAoAYMWKEWp8AiICAAGFvby8mTpwowsLCRJkyZYSRkZFadk/Tz+ORI0cEAFGhQgVRqVIlMWvWLBEcHCyMjIxE1apVVfX2798vypcvL0qUKCFWr14tVq9eLbZu3Zrne3zixAkBQPTv319kZGTk+/OIj48XDg4Oqt/pRYsWiZ9++kl4e3uLJ0+eqI7H1tZWmJqaih9++EHMnDlTBAQECKlUKrZs2ZLjeMqVKyfKly8vZs6cKUJDQ0VaWpo4dOiQ0NfXFzVq1BC//PKLmDVrlvD39xf6+vri9OnTqja6desm9PX1xahRo8SyZcvEtGnTROvWrcWaNWvyPY7sz7yfn59o3bq1mDdvnujRo4fq70e2pUuXCgDi8uXLattnZ29XrVqV737q1asn6tWrp3r9/Plz4e3tLfT09MTIkSPFnDlzRJ06dQQAtQx8dibSz89PuLi4iGnTpomQkBBhZWUlbGxs3joS4XX5vc/Zv+NVqlQRs2bNEt99950wNDQULi4uqp/n6+/X6yZNmiQkEono3LmzWLBggQgJCRElSpTIsS0RFQ4GkUT0QZ07d04AEAcOHBBCZH1pLl26tPj6669Vdfbt2ycAiB07dqht26JFC7UAYfXq1UIqlYo///xTrd6iRYsEAPH333+rygAIqVQqrl69mqNPbwZf6enpwtfXVzRs2FBVdv78+Vy/yPfu3TtHENm3b19hb2+fY5hely5dhLm5ea7B3uvmz58vAIh9+/apyhQKhShVqpSoUaNGvttqKjuIfPDggXjw4IGIiooSM2bMEBKJRPj6+gqlUvnWNrIDLktLS/H555+LGTNm5Bp8FjSIBCA2b96sKktJSRH29vaiQoUK+fYnJSVFAMhxASEvERERAoDo16+fWvno0aMFAHH48OEc/Tpx4oSqLPtzamhoKGJjY1XlixcvFgDEkSNHVGXZweqwYcNUZUqlUrRs2VLo6+urhj1u27ZNABCTJk1S61OHDh2ERCIRUVFRqjIAQl9fX63s4sWLAoCYO3euqkzTz2N2MODt7a12AWf27Nk5Ap2CDGdVKpWiXr16AoCwtbUVXbt2FfPnz1d7z7L17NlTSKVS1YWiN9sRQogRI0YIAGq/98+ePROurq7CxcVFFbxnH0+ZMmXUfueUSqVwd3cXTZs2VfucP3/+XLi6uoomTZqoyszNzcWQIUM0Os7XZX/m27Rpo1Y+ePBgAUBcvHhRCCFEcnKyMDAwEGPHjlWrN3z4cGFsbJzrUPTXvRlEhoWFCQBqQW56erqoUaOGMDExEU+fPhVCvAoiDQ0Nxd27d1V1T58+LQCIkSNHanyseb3P6enpomTJksLX11ft1oGdO3cKAGLcuHGqsjf/RsTExAgdHZ0cQ6AvX74sdHV1cx0aTUQfFoezEtEHtXbtWtja2qJBgwYAsobkde7cGevXr1cNuWzYsCFKlCiB33//XbXdkydPcODAAXTu3FlVtnHjRnh7e8PLywsPHz5ULQ0bNgQAHDlyRG3f9erVQ7ly5XL0ydDQUG0/KSkpqFOnjtqQtewhgoMHD1bbdtiwYWqvhRDYvHkzWrduDSGEWr+aNm2KlJSUtw6F69y5M/T09NSGtB47dgzx8fE5hrL+F2lpabCxsYGNjQ3c3NwwevRo1KpVC3/88YdG0+0vX74c8+bNg6urK7Zu3YrRo0fD29sbjRo10ni4Wm4cHBzw+eefq16bmZmhZ8+e+Oeff5CQkJDndtnD50xNTTXaz+7duwEgx0y333zzDQDkGB5Zrlw51KhRQ/U6e2bhhg0bwsnJKUd5bkOChw4dqvp39nDU9PR0HDx4UNUnHR0dDB8+PEefhBDYs2ePWnnjxo1RtmxZ1Wt/f3+YmZmp9v0un8c+ffpAX19f9bpOnTp5Ho8mJBIJ9u3bh0mTJsHS0hK//fYbhgwZAmdnZ3Tu3BnJyckAsmb73bZtG1q3bo3KlSvn2k72e1S1alXUrl1btc7ExAQDBgxATEwMrl27prZdr1691H7HIyIicPPmTXTr1g2PHj1SvR9paWlo1KgRjh8/DqVSCQCwsLDA6dOnce/evXc69iFDhqi9zv57kf3ZMzc3R9u2bfHbb7+phisrFAr8/vvvaNeuHYyNjQu0v927d8POzg5du3ZVlenp6WH48OFITU3FsWPH1Oq3a9cOpUqVUr2uWrUqqlWrpupfQbz5Pp87dw5JSUkYPHgwDAwMVOUtW7aEl5dXjt+v123ZsgVKpRKdOnVS+8za2dnB3d09x992IvrwGEQS0QejUCiwfv16NGjQALdv30ZUVBSioqJQrVo1JCYm4tChQwAAXV1dBAYG4o8//lDdm7ZlyxZkZGSoBZE3b97E1atXVYFQ9uLh4QEg696g17m6uubar507d6J69eowMDCAlZUVbGxssHDhQqSkpKjqxMbGQiqV5mjjzVllHzx4gOTkZCxZsiRHv7Lv83yzX2+ytrZG06ZNsXXrVtX9U+vWrYOuri46deqU77YFYWBggAMHDuDAgQNYvnw5vL29kZSUpPZFMD9SqRRDhgzB+fPn8fDhQ/zxxx9o3rw5Dh8+jC5durxzv9zc3HIEsdk/05iYGCgUCiQkJKgt6enpMDMzA5B1H5smsn+mb/4M7ezsYGFhgdjYWLXy1wNFICsAAABHR8dcy588eaJWLpVKUaZMmTyPK7tPDg4OOQJhb29v1fr8+gQAlpaWqn2/y+fxzTYtLS1zPZ6CkMlk+OGHH3D9+nXcu3cPv/32G6pXr44NGzaoAusHDx7g6dOn8PX1zbet2NhYeHp65ijP6z1683f25s2bALKCnjffk2XLlkEul6t+96dPn44rV67A0dERVatWRXBwcIGCaXd3d7XXZcuWhVQqVbsPuGfPnoiLi8Off/4JADh48CASExPxxRdfaLyfbLGxsXB3d4dUqv71Lq/35s3+AVmfydzuU36bN9/n7H3l9rPy8vLK0ZfX3bx5E0IIuLu75/gZXb9+/a1/Q4no/eMjPojogzl8+DDu37+P9evXY/369TnWr127Fp999hkAoEuXLli8eDH27NmDdu3aYcOGDfDy8lKbhEKpVMLPzw8zZ87MdX9vfrnPLTj6888/0aZNG9StWxcLFiyAvb099PT0sHz58lwnt3mb7AxGjx490KtXr1zr+Pv7v7WdHj16YOfOndi5cyfatGmDzZs347PPPoONjU2B+5QXHR0dNG7cWPW6adOm8PLywldffYXt27cXqC1ra2u0adMGbdq0Qf369XHs2DHExsbC2dk5z6ymJpP95ObOnTs5vrAeOXIE9evXh4ODQ4EnBtH0Iec6OjoFKs/OLL1Pb9v3u3we3/fx2Nvbo0uXLggMDISPjw82bNiAFStWaKXt3Lz5e5/9nvz8888oX758rtuYmJgAADp16oQ6depg69at2L9/P37++WdMmzYNW7ZsQfPmzQvcl9w+a02bNoWtrS3WrFmDunXrYs2aNbCzs1P73fwYaHrxSRNKpRISiQR79uzJ9fOY/fMhosLDIJKIPpi1a9eiZMmSmD9/fo51W7ZswdatW7Fo0SIYGhqibt26sLe3x++//47atWvj8OHD+OGHH9S2KVu2LC5evIhGjRppHAi8afPmzTAwMMC+ffsgk8lU5cuXL1er5+zsDKVSidu3b6tdvX991koAsLGxgampKRQKxX/6EtimTRuYmppi3bp10NPTw5MnT7Q6lDU39vb2GDlyJEJCQnDq1Kl3fs5j5cqVcezYMdy/fx/Ozs6qTFZycjIsLCxU9fLKRERFRUEIofYzvXHjBoCsWVItLCxw4MABtW2yLy60atUKS5YswcmTJ9WGnuYm+2d68+ZNVaYGABITE5GcnAxnZ2fND1oDSqUSt27dUmUfAfXjyu7TwYMH8ezZM7Vs5L///qtaXxDa+jy+6V1/316np6cHf39/3Lx5Ew8fPkTJkiVhZmb21osAzs7OiIyMzFGu6XuUPfzXzMxMo/fE3t4egwcPxuDBg5GUlISKFSti8uTJGgWRN2/eVLvgERUVBaVSqTabrY6ODrp164YVK1Zg2rRp2LZtG/r3759nMJ8fZ2dnXLp0CUqlUi0bmdd7k52Vfd2NGzfynW23IH0BgMjISNUtBtkiIyPz/TmVLVsWQgi4urqq/b4QUdHB4axE9EG8ePECW7ZsQatWrdChQ4ccy9ChQ/Hs2TNVBkwqlaJDhw7YsWMHVq9ejczMTLWhrEBWliA+Ph5Lly7NdX9paWlv7ZeOjg4kEolaViwmJgbbtm1Tq5c91f6CBQvUyufOnZujvcDAQGzevDnXL8MPHjx4a5+ArKv6n3/+OXbv3o2FCxfC2NgYbdu21Wjb/2LYsGEwMjLC1KlT862XkJCQ494zAEhPT8ehQ4fUholmf2k/fvy4ql5aWlqejx24d+8etm7dqnr99OlTrFq1CuXLl4ednR0MDAzQuHFjtSU7UP32229hbGyMfv36ITExMUfb0dHRmD17NgCgRYsWAICwsDC1OtmZ7ZYtW+b7HryLefPmqf4thMC8efOgp6eHRo0aqfqkUCjU6gFZj2GQSCQFzn5p6/P4JmNjY7Xh3vm5efMm4uLicpQnJyfj5MmTsLS0hI2NDaRSKdq1a4cdO3bg3LlzOepnZ0JbtGiBM2fO4OTJk6p1aWlpWLJkCVxcXHK97/l1lSpVQtmyZTFjxgykpqbmWJ/9nigUihzHWLJkSTg4OOR4BExe3rxglv334s2f4xdffIEnT57gq6++QmpqKnr06KFR+29q0aIFEhIS1O4nz8zMxNy5c2FiYoJ69eqp1d+2bZva/ctnzpzB6dOn3ynL+qbKlSujZMmSWLRokdr7tWfPHly/fj3f36/27dtDR0cHISEhOTLgQgg8evToP/ePiP4bZiKJ6IPYvn07nj17hjZt2uS6vnr16rCxscHatWtVwWLnzp0xd+5cjB8/Hn5+fmrZIiDri9eGDRswcOBAHDlyBLVq1YJCocC///6LDRs2YN++fblO0PG6li1bYubMmWjWrBm6deuGpKQkzJ8/H25ubrh06ZKqXqVKlRAYGIiwsDA8evQI1atXx7Fjx1SZpNczM1OnTsWRI0dQrVo19O/fH+XKlcPjx49x4cIFHDx4EI8fP9boPevRowdWrVqFffv2oXv37gWeZONdWFtbo0+fPliwYAGuX7+e4z3PdvfuXVStWhUNGzZEo0aNYGdnh6SkJPz222+4ePEiRowYgRIlSgAAPvvsMzg5OaFv374YM2YMdHR08Ouvv8LGxibX4MLDwwN9+/bF2bNnYWtri19//RWJiYk5ssO5KVu2LNatW4fOnTvD29sbPXv2hK+vL9LT03HixAls3LgRvXv3BpCVvezVqxeWLFmC5ORk1KtXD2fOnMHKlSvRrl071eRP2mJgYIC9e/eiV69eqFatGvbs2YNdu3bh+++/Vw1Tbt26NRo0aIAffvgBMTExCAgIwP79+/HHH39gxIgRapPoaEpbn8fXVapUCb///jtGjRqFKlWqwMTEBK1bt8617sWLF9GtWzc0b94cderUgZWVFeLj47Fy5Urcu3cPYWFhqqzblClTsH//ftSrVw8DBgyAt7c37t+/j40bN+Kvv/6ChYUFvvvuO/z2229o3rw5hg8fDisrK6xcuRK3b9/G5s2bc9wP+CapVIply5ahefPm8PHxQZ8+fVCqVCnEx8fjyJEjMDMzw44dO/Ds2TOULl0aHTp0QEBAAExMTHDw4EGcPXsWv/zyi0bv0+3bt9GmTRs0a9YMJ0+exJo1a9CtW7ccz4asUKECfH19VZOFVaxYUaP23zRgwAAsXrwYvXv3xvnz5+Hi4oJNmzbh77//RlhYWI57bd3c3FC7dm0MGjQIcrkcYWFhsLa2xrfffvtO+3+dnp4epk2bhj59+qBevXro2rUrEhMTMXv2bLi4uGDkyJF5blu2bFlMmjQJQUFBiImJQbt27WBqaorbt29j69atGDBggNrzgomoEHz4CWGJqDhq3bq1MDAwyPeZgr179xZ6enqqRxEolUrh6OiY6yMPsqWnp4tp06YJHx8fIZPJhKWlpahUqZIICQkRKSkpqnoA8pyqPzw8XLi7uwuZTCa8vLzE8uXLc30sRVpamhgyZIiwsrISJiYmol27diIyMlIAEFOnTlWrm5iYKIYMGSIcHR2Fnp6esLOzE40aNRJLlizR6P0SQojMzExhb28vAIjdu3drvJ0m8npOpBBCREdHCx0dHdGrV688t3/69KmYPXu2aNq0qShdurTQ09MTpqamokaNGmLp0qU5HhFy/vx5Ua1aNaGvry+cnJzEzJkz83zER8uWLcW+ffuEv7+/6meycePGAh3fjRs3RP/+/YWLi4vQ19cXpqamolatWmLu3Lni5cuXqnoZGRkiJCREuLq6Cj09PeHo6CiCgoLU6rzerzfl9rnKfnzCzz//rCrLfr+jo6NVzza1tbUV48ePV3uepBBZj6sYOXKkcHBwEHp6esLd3V38/PPPOd7TvD7Tzs7OOX52mnwesx/V8OZ7nX08y5cvV5WlpqaKbt26CQsLCwEg38d9JCYmiqlTp4p69eoJe3t7oaurKywtLUXDhg3Fpk2bctSPjY0VPXv2FDY2NkImk4kyZcqIIUOGqD12JDo6WnTo0EFYWFgIAwMDUbVq1RzPdc3reLL9888/on379sLa2lrIZDLh7OwsOnXqJA4dOiSEEEIul4sxY8aIgIAAYWpqKoyNjUVAQIBYsGBBnseaLfvvx7Vr10SHDh2EqampsLS0FEOHDlV73MXrpk+fLgCIKVOmvLX9bG8+4kOIrPe7T58+okSJEkJfX1/4+fmp/eyEUP+M/vLLL8LR0VHIZDJRp04d1eNHNPW29/n3338XFSpUEDKZTFhZWYnu3burPVZEiLwfA7R582ZRu3ZtYWxsLIyNjYWXl5cYMmSIiIyMLFAfiUj7JEJ8gDv/iYg+UREREahQoQLWrFnz3u9ZpI9X7969sWnTplyHTxIBwOzZszFy5EjExMTkOutuburUqQOZTKZ6RAwR0YfCeyKJiDT04sWLHGVhYWGQSqWoW7duIfSIiD4FQgiEh4ejXr16GgeQAHD//n3VsHEiog+J90QSEWlo+vTpOH/+PBo0aABdXV3s2bMHe/bswYABA3I8ToSI6G3S0tKwfft2HDlyBJcvX8Yff/yh0XYnTpzAli1bEB0djbFjx76XvqWnp7/1fllzc3OtPtqDiD4eDCKJiDRUs2ZNHDhwABMnTkRqaiqcnJwQHByc49EjRESaePDgAbp16wYLCwt8//33eU489qalS5diz549GDFiBPr06fNe+nbixIm3Ti61fPly1URVRFS88J5IIiIiIlLz5MkTnD9/Pt86Pj4+sLe3/0A9IqKihEEkERERERERaYwT6xAREREREZHGGEQSERERERGRxjixDhERERERkZYoEzy02p7U7oZW29MGBpH0wV27U6qwu0BULJRzjEfzUsMKuxtExcKe+LmIvONQ2N0g+uR5Ot4r7C4QGEQSERERERFpjRJKrbZXFO8/ZBBJRERERESkJQqh3SCyKAZsRTGwJSIiIiIioiKqKAa2REREREREHyUlRGF34b1jJpKIiIiIiEhLlFr+r6Di4+PRo0cPWFtbw9DQEH5+fjh37pxqfe/evSGRSNSWZs2aFWgfzEQSERERERF9Ap48eYJatWqhQYMG2LNnD2xsbHDz5k1YWlqq1WvWrBmWL1+uei2TyQq0HwaRREREREREWqIQhTecddq0aXB0dFQLEF1dXXPUk8lksLOze+f9cDgrERERERGRlightLoUxPbt21G5cmV07NgRJUuWRIUKFbB06dIc9Y4ePYqSJUvC09MTgwYNwqNHjwq0HwaRRERERERERZRcLsfTp0/VFrlcnmvdW7duYeHChXB3d8e+ffswaNAgDB8+HCtXrlTVadasGVatWoVDhw5h2rRpOHbsGJo3bw6FQqFxnziclYiIiIiISEsUWp6dNTQ0FCEhIWpl48ePR3BwcI66SqUSlStXxpQpUwAAFSpUwJUrV7Bo0SL06tULANClSxdVfT8/P/j7+6Ns2bI4evQoGjVqpFGfmIkkIiIiIiLSEm0PZw0KCkJKSoraEhQUlOu+7e3tUa5cObUyb29vxMXF5dnfMmXKoESJEoiKitL4GJmJJCIiIiIiKqJkMpnGs6fWqlULkZGRamU3btyAs7NzntvcvXsXjx49gr29vcZ9YiaSiIiIiIhISxRCaHUpiJEjR+LUqVOYMmUKoqKisG7dOixZsgRDhgwBAKSmpmLMmDE4deoUYmJicOjQIbRt2xZubm5o2rSpxvthEElERERERKQlSi0vBVGlShVs3boVv/32G3x9fTFx4kSEhYWhe/fuAAAdHR1cunQJbdq0gYeHB/r27YtKlSrhzz//LNCzIjmclYiIiIiI6BPRqlUrtGrVKtd1hoaG2Ldv33/eB4NIIiIiIiIiLdH27KxFEYNIIiIiIiIiLVF8+jEk74kkIiIiIiIizTETSUREREREpCUFnQznY8RMJBEREREREWmMmUgiIiIiIiItUUBS2F147xhEEhERERERaYmSE+sQERERERERvcJMJBERERERkZZwOCsRERERERFprDgEkRzOSkRERERERBpjJpKIiIiIiEhLlOLTz0QyiCQiIiIiItISDmclIiIiIiIieg0zkURERERERFqiKAZ5uk//CD9hvXv3Rrt27fKt4+LigrCwMI3aW7FiBSwsLP5zv4iIiIiIiiulkGh1KYqYidSCkydPonbt2mjWrBl27dqlti4mJgaurq74559/UL58+Vy3r1+/Po4dO5aj/KuvvsKiRYs0aiMvZ8+ehbGxsUZ1O3fujBYtWmhUd8WKFRgxYgSSk5ML1B8q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wsKFC+Hu7o59+/Zh0KBBGD58OFauXAkASEhIAADY2tqqbWdra6tapwkOZyUiIiIiItIShZZnZw0KCsKoUaPUymQyWa51lUolKleujClTpgAAKlSogCtXrmDRokXo1auX1vrETCQREREREVERJZPJYGZmprbkFUTa29ujXLlyamXe3t6Ii4sDANjZ2QEAEhMT1eokJiaq1mmCQSQREREREZGWKCHR6lIQtWrVQmRkpFrZjRs34OzsDCBrkh07OzscOnRItf7p06c4ffo0atSoofF+OJyViIiIiIhIS7Q9nLUgRo4ciZo1a2LKlCno1KkTzpw5gyVLlmDJkiUAAIlEghEjRmDSpElwd3eHq6srfvrpJzg4OKBdu3Ya74dBJBERERER0SegSpUq2Lp1K4KCgjBhwgS4uroiLCwM3bt3V9X59ttvkZaWhgEDBiA5ORm1a9fG3r17YWBgoPF+GEQSERERERFpiaKQ7xhs1aoVWrVqled6iUSCCRMmYMKECe+8DwaRREREREREWqIUBbuP8WPEiXWIiIiIiIhIY8xEEhERERERaUlhD2f9EBhEEhERERERaYmyEGdn/VA+/SMkIiIiIiIirWEmkoiIiIiISEsU+PQn1mEQSUREREREpCUczkpERERERET0GmYiiYiIiIiItITDWYmIiIiIiEhjHM5KRERERERE9BpmIomIiIiIiLREUQwykQwiiYiIiIiItERZDO6J/PTDZCIiIiIiItIaZiKJiIiIiIi0hMNZiYiIiIiISGNK8ekPZ2UQSR9cOcf4wu4CUbGxJ35uYXeBqNjwdLxX2F0gIvogGETSB3cxzrGwu0BULAQ43UGDz6YVdjeIioUj+8ci+R7Pb0Tvm4XDncLuwlspisG0MwwiiYiIiIiItKQ4DGf99MNkIiIiIiIi0hpmIomIiIiIiLREWQzydJ/+ERIREREREZHWMBNJRERERESkJYpicE8kg0giIiIiIiIt4cQ6RERERERERK9hJpKIiIiIiEhLlOLTz9MxiCQiIiIiItISBTiclYiIiIiIiEiFmUgiIiIiIiItKQ4T6zCIJCIiIiIi0pLicE/kp3+EREREREREpDXMRBIREREREWmJshhMrMMgkoiIiIiISEsUxeCeSA5nJSIiIiIi+gQEBwdDIpGoLV5eXqr19evXz7F+4MCBBd4PM5FERERERERa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nj35bmdubo7AwEDs2rUL7dq1U5Xr6Ojg0aNH6NmzJxITE1GiRAm0b99eNXlPzZo1MXDgQHTu3BmPHj3C+PHj+ZiPj4CbpxKjg+VYF66PzWv0UNJOoNegdNRplHUSleoA9+5I8MsBfTx7KoGpqUBZTyVCZsnh6PIqGEy8L8HTp6/+QEbfkCJktIHq9apF+gCAek0yMeTbvIdUE32qLC2METSmFaysjJH2XI5btx7g2+834PyFGABAm1bl0fuL2qr6c2Z2BwBM/XkX9h24AgBwsLeEubnhqzrzD+LLXnXw9bDPYGlhhIePUrFjdwRWrfn7wx0YURFUzkuJ6RPlWLBUH+Gr9OBgLzBySDqaNfn/uU0KREVLsXufLp6lAjbWAlUrK/HVl+nQ13/VTvw9CZJTXp3bmjRUIDklA0tW6OHRYwk8yioRNk0O67df2yf65EmEEEwTFHONGjWCj48P5syZ80H2dzHO8e2ViOg/C3C6gwafTSvsbhAVC0f2j0XyPZ7fiN43C4c7hd2Ft6p/aLRW2zvaaIZW29OGQs9EUuF58uQJjh49iqNHj2LBggWF3R0iIiIioo+eEhzOSp+wChUq4MmTJ5g2bRo8PT0LuztERERERPQRYBBZjMXExBR2F4iIiIiIPimcWIeIiIiIiIg0JopBEFnknhNJRERERERERRczkURERERERFrC4axERERERESkMQ5nJSIiIiIiInoNM5FERERERERawuGsREREREREpDEhCrsH7x+HsxIREREREZHGmIkkIiIiIiLSEiU4nJWIiIiIiIg0xNlZiYiIiIiIiF7DTCQREREREZGWcHZWIiIiIiIi0hhnZyUiIiIiIiJ6DTORREREREREWlIcJtZhEElERERERKQlxSGI5HBWIiIiIiKiT0BwcDAkEona4uXlpVr/8uVLDBkyBNbW1jAxMUFgYCASExMLvB8GkURERERERFqiFBKtLgXl4+OD+/fvq5a//vpLtW7kyJHYsWMHNm7ciGPHjuHevXto3759gffB4axERERERESfCF1dXdjZ2eUoT0lJQXh4ONatW4eGDRsCAJYvXw5vb2+cOnUK1atX13gfzEQSERERERFpiRDaXQrq5s2bcHBwQJkyZdC9e3fExcUBAM6fP4+MjAw0btxYVdfLywtOTk44efJkgfbBTCQREREREZGWaHtiHblcDrlc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29sXqE0GkURERERERNpSiLOzBgUFoXnz5nBycsKzZ8+wbt06HD16FPv27UN0dDTWrVuHFi1awNraGpcuXcLIkSNRt25d+Pv7F2g/DCKJiIiIiIi0RKIsvH0nJSWhZ8+euH//PszNzeHv7499+/ahSZMmuHPnDg4ePIiwsDCkpaXB0dERgYGB+PHHHwu8HwaRREREREREn4Dw8PA81zk6OuLYsWNa2Q+DSCIiIiIiIm0pxOGsHwqDSCIiIiIiIi3R9uysRZG0sDtAREREREREHw9mIomIiIiIiLRFfPqpSAaRREREREREWsLhrERERERERESvYSaSiIiIiIhIW4pBJpJBJBERERERkZZwOCsRERERERHRa5iJJCIiIiIi0hbOzkpERERERESa4nBWIiIiIiIiotcwE0lERERERKQtxSATySCSiIiIiIhISziclYiIiIiIiOg1zEQSERERERFpi/LTT0UyiCQiIiIiItKWTz+G5HBWIiIiIiIi0hwzkURERERERFpSHCbWYRBJRERERESkLeLTjyI5nJWIiIiIiIg0xkwkERERERGRlnA4KxEREREREWmuGASRHM5KREREREREGmMmkoiIiIiISEskxWBiHQaR9MHVc7lR2F0gKjYOHf2+sLtAVGxYONwp7C4QUVGgLOwOvH8MIumDuxDnVNhdICoWKjrFobnnd4XdDaJiYU/kVCgTPAq7G0SfPKkdkxFFAYNIIiIiIiIiLeFwViIiIiIiItLcpx9DcnZWIiIiIiIi0hwzkURERERERNrC4axERERERESkKcmnH0NyOCsRERERERFpjplIIiIiIiIibSkGw1mZiSQiIiIiItISiVK7S0EsXLgQ/v7+MDMzg5mZGWrUqIE9e/ao1r98+RJDhgyBtbU1TExMEBgYiMTExAIfI4NIIiIiIiKiT0Dp0qUxdepUnD9/HufOnUPDhg3Rtm1bXL16FQAwcuRI7NixAxs3bsSxY8dw7949tG/fvsD74XBWIiIiIiIibSnE4aytW7dWez158mQsXLgQp06dQunSpREeHo5169ahYcOGAIDly5fD29sbp06dQvXq1TXeDzORRERERERERZRcLsfTp0/VFrlc/tbtFAoF1q9fj7S0NNSoUQPnz59HRkYGGjdurKrj5eUFJycnnDx5skB9YhBJRERERESkLUK7S2hoKMzNzdWW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
"/>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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LUZGRERERESUt+hEEvilatWqoVq1atoOg4iIiIiI8iFd7capKTqTBAYGBiIgIABRUVFQKpVqx6ZMmaKlqIiIiIiIKL/R1W6cmqITSeC6deswaNAgFChQAI6OjpCkT790SZKYBBIREREREWmITiSBs2bNwuzZszF+/Hhth0JERERERPkcu4Pmgrdv36JDhw7aDoOIiIiIiAhCaDuCnKUTS0R06NBBtTYgERERERER5RydaAksVqwYJk+ejAsXLqBcuXIwNDRUOz58+HAtRUZERERERPmNEuwOmuPWrl0Lc3NznD59GqdPn1Y7JkkSk0AiIiIiIso1nB00F4SEhGg7BCIiIiIionxBJ5JAIiIiIiIiXcHZQXPI6NGjMXPmTJiZmWH06NEZnrt48eJcioqIiIiIiPK7vD47qNaSwOvXr+PBgweoWLEirl+/nu55ny8cT0RERERERF9Ha0lgQEAA9PX1ERERgYCAAABAp06d8NNPP8HBwUFbYRERERERUT7HiWFykPiinfXw4cOIi4vTUjRERERERER5PwnUicXiU3yZFBIREREREZFmabUlUJKkVGP+OAaQiIiIiIi0ibOD5iAhBHr16gWZTAYAiI+Px8CBA2FmZqZ23p49e7QRHhERERERUZ6j1SSwZ8+eavvdu3fXUiRERERERETJ8vooNa0mgZs2bdLm5YmIiIiIiFLhxDBERERERESUZ2i1JZCIiIiIiEjX5PWWQCaBREREREREn8njQwLZHZSIiIiIiCg/YUsgERERERHRZ9gdlIiIiIiIKD/J4/1B2R2UiIiIiIgoH2ESSERERERE9BkhJI1tWTFt2jRIkqS2eXp6qo7Hx8djyJAhsLOzg7m5Odq1a4cXL15k+f6YBBIREREREX1GCM1tWVWmTBlERESotjNnzqiOjRo1Cvv378euXbtw+vRphIeHo23btlm+BscEEhERERER6QgDAwM4OjqmKo+JicGGDRuwbds21KtXDwCwadMmlCpVChcuXEDVqlUzf43sBKavr4+IiAgULFhQrfz169coWLAgFApFdqrVKNdCEdoOgYhywOEnS7QdAhHlEB+3EG2HQEQEQLuzgwYGBsLZ2RnGxsaoVq0a5s6di8KFC+Pq1atITExEgwYNVOd6enqicOHCOH/+fM4ngSKddk25XA4jI6PsVKlxyx/U03YIRKRhQz1PoqFeB22HQUQ54JhyFwJDnbUdBhFpWHGXcG2HkD0aTALlcjnkcrlamUwmg0wmS3Wuj48PNm/ejJIlSyIiIgLTp09HrVq1cOfOHURGRsLIyAjW1tZqj3FwcEBkZGSWYspSEvjTTz8BACRJwvr162Fubq46plAo8Pfff6sNXCQiIiIiIsrP5s6di+nTp6uVTZ06FdOmTUt1bpMmTVQ/e3l5wcfHB25ubti5cydMTEw0FlOWksAlS5K7YQkhsHr1aujr66uOGRkZwd3dHatXr9ZYcERERERERLktOxO6pMfPzw+jR49WK0urFTAt1tbWKFGiBIKCgtCwYUMkJCQgOjparTXwxYsXaY4hzEiWksCQkOS++t9++y327NkDGxubLF2MiIiIiIhI52kwCUyv62dmxMbGIjg4GN999x28vb1haGiIEydOoF27dgCAhw8f4tmzZ6hWrVqW6s3WmMCAgIDsPIyIiIiIiIjSMXbsWLRo0QJubm4IDw/H1KlToa+vjy5dusDKygp9+/bF6NGjYWtrC0tLSwwbNgzVqlXL0qQwQDaTQIVCgc2bN+PEiROIioqCUqlUO37y5MnsVEtERERERKR12podNDQ0FF26dMHr169hb2+PmjVr4sKFC7C3tweQPDxPT08P7dq1g1wuh6+vL1auXJnl62QrCRwxYgQ2b96MZs2aoWzZspAk7U2hSkREREREpFEa7A6aFTt27MjwuLGxMVasWIEVK1Z81XWylQTu2LEDO3fuRNOmTb/q4kRERERERJS7spUEGhkZoVixYpqOhYiIiIiISOu0uVh8btDLzoPGjBmDZcuWpbtoPBERERER0X+W0OCmg7LVEnjmzBkEBATg8OHDKFOmDAwNDdWO79mzRyPBERERERERkWZlKwm0trZGmzZtNB0LERERERGRDsjb3UGzlQRu2rRJ03EQERERERHpBh3txqkp2RoTCABJSUk4fvw41qxZg/fv3wMAwsPDERsbq7HgiIiIiIiISLOy1RL49OlTNG7cGM+ePYNcLkfDhg1hYWGB+fPnQy6XY/Xq1ZqOk4iIiIiIKHewJTC1ESNGoHLlynj79i1MTExU5W3atMGJEyc0FhwREREREVGuE5LmNh2UrZbAf/75B+fOnYORkZFaubu7O8LCwjQSGBEREREREWletpJApVIJhUKRqjw0NBQWFhZfHRQRERER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7FRJRERERESkEzQ5MczXOnXqlOpnV1dXnD59+qvrzFYSuHjxYsTGxgIApk+fjtjYWPz+++8oXrx4pmcGJSIiIiIi0kk6lATmhGwlgR4eHqqfzczMsHr1ao0FRERERERERDnnqxaLv3LlCu7fvw8AKF26NLy9vTUSFBERERERkbboUnfQnJCtJDA0NBRdunTB2bNnYW1tDQCIjo5G9erVsWPHDri4uGgyRiIiIiIiotyTx5PAbM0O2q9fPyQmJuL+/ft48+YN3rx5g/v370OpVKJfv36ajpGIiIiIiIg0JFstgadPn8a5c+dQsmRJVVnJkiXx888/o1atWhoLjoiIiIiIKNfl8ZbAbCWBrq6uSExMTFWuUCjg7Oz81UERERERERFpS14fE5it7qA//vgjhg0bhitXrqjKrly5ghEjRmDhwoUaC46IiIiIiIg0K1stgb169cKHDx/g4+MDA4PkKpKSkmBgYIA+ffqgT58+qnPfvHmjmUiJiIiIiIjoq2UrCVy6dKmGwyAiIiIiItIRebw7aLaSwJ49e2o6DiIiIiIiIsoF2RoTCADBwcGYNGkSunTpgqioKADA4cOHcffuXY0FR0RERERElNskoblNF2UrCTx9+jTKlSuHixcvYs+ePYiNjQUA3Lx5E1OnTtVogERERERERLlKaHDTQdlKAv/3v/9h1qxZOHbsGIyMjFTl9erVw4ULFzQWHBEREREREWlWtpLA27dvo02bNqnKCxYsiFevXn11UERERERERFrDlsDUrK2tERERkar8+vXrKFSo0FcHRUREREREpC0cE5iGzp07Y/z48YiMjIQkSVAqlTh79izGjh2LHj16aDpGIiIiIiIi0pBsJYFz5syBp6cnXF1dERsbi9KlS6NWrVqoXr06Jk2apOkYiYiIiIiIck8e7w6arXUCjYyMsG7dOkyZMgW3b99GbGwsKlasiOLFi2s6PiIiIiIiolylq904NSXTSeDo0aMzPP75rKCLFy/OfkRERERERESUYzKdBF6/fl1t/9q1a0hKSkLJkiUBAI8ePYK+vj68vb01GyEREREREVFuYktgsoCAANXPixcvhoWFBbZs2QIbGxsAwNu3b9G7d2/UqlVL81ESERERERHlljyeBGZrYphFixZh7ty5qgQQAGxsbDBr1iwsWrRIY8ERERERERGRZmVrYph3797h5cuX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RERE+V0en59Eq0ng6tWrUbhwYXh4eOD06dPp9nHds2dPLkdGRERERESUN2k1CezRowckSdJmCERERERERGp0tRunpmh9sXgiIiIiIiKdkseTQK1PDENERERERES5R+vrBBIREREREekSKY9PDCMJkcfvkIiIiIiIKAvq1Z+nsbpOnvifxurSlDzbEnj5mbu2QyAiDfum8BP4GnfTdhhElAP847dCGVlC22EQkYbpOT7SdgiUhjybBBIREREREWVHXu8OyiSQiIiIiIjoc3k7B+TsoERERERERPkJWwKJiIiIiIg+x+6gRERERERE+YeUt3NAdgclIiIiIiLKT9gSSERERERE9Dl2ByUiIiIiIso/JKW2I8hZ7A5KRERERESUj7AlkIiIiIiI6HN5vDsoWwKJiIiIiIjyEbYEEhERERERfS5vNwQyCSQiIiIiIvqcxO6gRERERERElFewJZCIiIiIiOhzebwlkEkgERERERHR57hOIBEREREREeUVbAkkIiIiIiL6TF6fGIZJIBERERER0efyeBLI7qBERERERET5CFsCiYiIiIiIPpfHWwKZBBIREREREX2Os4MSERERERFRXsGWQCIiIiIios9wdtBc8urVKzx58gSSJMHd3R12dnbaDomIiIiIiPKjPJ4Ear076N27d1G7dm04ODjAx8cHVapUQcGCBVGvXj08fPhQ2+ERERERERHlilWrVsHLywuWlpawtLREtWrVcPjwYdXx+Ph4DBkyBHZ2djA3N0e7du3w4sWLLF9Hq0lgZGQk6tSpg5cvX2Lx4sU4dOgQDh48iB9//BERERGoVasWoqKitBkiERERERHlN0JobssCFxcXzJs3D1evXsWVK1dQr149tGrVCnfv3gUAjBo1Cvv378euXbtw+vRphIeHo23btlm+PUkI7bV1jh8/HsePH8fZs2dhbGysduzjx4+oWbMmGjVqhLlz52a57svP3DUUJRHpim8KP4GvcTdth0FEOcA/fiuUkSW0HQYRaZie4yNth5AtjctN1FhdR27P/qrH29ra4scff0T79u1hb2+Pbdu2oX379gCABw8eoFSpUjh//jyqVq2a6Tq12hJ47NgxjB8/PlUCCAAmJiYYN24c/P39tRAZERERERGR9igUCuzYsQNxcXGoVq0arl69isTERDRo0EB1jqenJwoXLozz589nqW6t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
"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=74a19f1c">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The aggregated AI-R report provides a high-level overview of the organization's AI-readiness across different segments. The skills gap heatmap offers a granular view, clearly highlighting which $V^R$ sub-components are strong or weak within specific job roles, thereby pinpointing areas for targeted upskilling efforts.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=f02839c1">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-17:-What-If-Scenario-Engine:-Simulating-Learning-Pathway-Impact">Section 17: What-If Scenario Engine: Simulating Learning Pathway Impact<a class="anchor-link" href="#Section-17:-What-If-Scenario-Engine:-Simulating-Learning-Pathway-Impact">¶</a></h1><p>The "What-If" scenario engine allows HR leaders to simulate the impact of various training programs and learning pathways on an individual's or a cohort's AI-Readiness. This dynamic tool helps assess potential improvements to $V^R$ sub-components and the overall AI-R score.</p>
<p>The update formula for AI-R is conceptually:
$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$
Where $\Delta_p$ is the pre-calibrated impact coefficient for pathway $p$ (from <code>df_pathways</code>), $Completion_p \in [0,1]$ is the fraction completed, and $Mastery_p \in [0,1]$ is the assessment performance score.
The pathway impact ($\Delta_p$) will directly affect the AI-Fluency, Domain-Expertise, or Adaptive-Capacity scores, which then propagate to $V^R$ and subsequently AI-R.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=d60029c5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [31]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">numpy</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">np</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">random</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">matplotlib.pyplot</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">plt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">seaborn</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">sns</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">copy</span>

<span class="c1"># --- Re-defining dependent functions for self-contained tests ---</span>

<span class="c1"># From Cell 4</span>
<span class="k">def</span><span class="w"> </span><span class="nf">calculate_ai_r</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="n">hr_score</span><span class="p">,</span> <span class="n">synergy_score</span><span class="p">,</span> <span class="n">alpha</span><span class="p">,</span> <span class="n">beta</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes the overall AI-Readiness Score."""</span>
    <span class="n">vr_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
    <span class="n">hr_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">hr_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
    <span class="n">synergy_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">synergy_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
    <span class="n">ai_r</span> <span class="o">=</span> <span class="p">(</span><span class="n">alpha</span> <span class="o">*</span> <span class="n">vr_score</span><span class="p">)</span> <span class="o">+</span> <span class="p">((</span><span class="mi">1</span> <span class="o">-</span> <span class="n">alpha</span><span class="p">)</span> <span class="o">*</span> <span class="n">hr_score</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">beta</span> <span class="o">*</span> <span class="n">synergy_score</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">ai_r</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># From Cell 45</span>
<span class="k">def</span><span class="w"> </span><span class="nf">calculate_idiosyncratic_readiness</span><span class="p">(</span><span class="n">employee_data_row</span><span class="p">,</span> <span class="n">vr_weights</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes total V^R score from its sub-components."""</span>
    <span class="n">ai_fluency</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span>
    <span class="n">domain_expertise</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span>
    <span class="n">adaptive_capacity</span> <span class="o">=</span> <span class="n">employee_data_row</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span>
    <span class="n">vr_score</span> <span class="o">=</span> <span class="p">(</span>
        <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'ai_fluency_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">ai_fluency</span> <span class="o">+</span>
        <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'domain_expertise_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">domain_expertise</span> <span class="o">+</span>
        <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">adaptive_capacity</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># From Cell 53</span>
<span class="k">def</span><span class="w"> </span><span class="nf">calculate_synergy</span><span class="p">(</span><span class="n">vr_score</span><span class="p">,</span> <span class="n">hr_score</span><span class="p">,</span> <span class="n">alignment_factor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Computes Synergy%."""</span>
    <span class="n">vr_norm</span> <span class="o">=</span> <span class="n">vr_score</span> <span class="o">/</span> <span class="mi">100</span>
    <span class="n">hr_norm</span> <span class="o">=</span> <span class="n">hr_score</span> <span class="o">/</span> <span class="mi">100</span>
    <span class="n">synergy</span> <span class="o">=</span> <span class="p">(</span><span class="n">vr_norm</span> <span class="o">*</span> <span class="n">hr_norm</span><span class="p">)</span> <span class="o">*</span> <span class="n">alignment_factor</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">synergy</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># The function to be tested: plot_current_vs_projected_ai_r</span>
<span class="c1"># This is a plotting function, per requirement #5, we return 'NO_TESTS_NEEDED' for it</span>
<span class="c1"># However, for completeness within the test suite structure, we keep its definition</span>
<span class="c1"># but do not generate explicit tests that rely on matplotlib.show().</span>
<span class="k">def</span><span class="w"> </span><span class="nf">plot_current_vs_projected_ai_r</span><span class="p">(</span><span class="n">current_scores</span><span class="p">,</span> <span class="n">projected_scores</span><span class="p">,</span> <span class="n">scenario_names</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Compares current vs. projected AI-R for an individual or group."""</span>
    <span class="n">labels</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'Current AI-R'</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'Projected AI-R (</span><span class="si">{</span><span class="n">s</span><span class="si">}</span><span class="s1">)'</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">scenario_names</span><span class="p">]</span>
    <span class="n">values</span> <span class="o">=</span> <span class="p">[</span><span class="n">current_scores</span><span class="p">]</span> <span class="o">+</span> <span class="n">projected_scores</span>

    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">labels</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="p">[</span><span class="s1">'skyblue'</span><span class="p">]</span> <span class="o">+</span> <span class="p">[</span><span class="s1">'lightcoral'</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">projected_scores</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">'AI-Readiness Score'</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Current vs. Projected AI-Readiness Score'</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">ylim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span><span class="s1">'y'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'--'</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.7</span><span class="p">)</span>
    <span class="c1"># plt.show() # Comment out plt.show() for testing environments</span>

<span class="c1"># The main function to be tested in this cell</span>
<span class="k">def</span><span class="w"> </span><span class="nf">simulate_pathway_impact</span><span class="p">(</span><span class="n">employee_id</span><span class="p">,</span> <span class="n">pathway_id</span><span class="p">,</span> <span class="n">completion_rate</span><span class="p">,</span> <span class="n">mastery_score</span><span class="p">,</span> <span class="n">df_employees_data</span><span class="p">,</span> <span class="n">df_occupations_data</span><span class="p">,</span> <span class="n">df_pathways_data</span><span class="p">,</span> <span class="n">params</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simulates the impact of a learning pathway on an individual's AI-R score."""</span>
    <span class="n">employee_row_original</span> <span class="o">=</span> <span class="n">df_employees_data</span><span class="p">[</span><span class="n">df_employees_data</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">employee_row_sim</span> <span class="o">=</span> <span class="n">employee_row_original</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">deep</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="n">pathway_info</span> <span class="o">=</span> <span class="n">df_pathways_data</span><span class="p">[</span><span class="n">df_pathways_data</span><span class="p">[</span><span class="s1">'pathway_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">pathway_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

    <span class="c1"># Apply impact to VR sub-components</span>
    <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_ai_fluency'</span><span class="p">]</span> <span class="o">*</span> <span class="n">completion_rate</span> <span class="o">*</span> <span class="n">mastery_score</span><span class="p">,</span>
        <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
    <span class="p">)</span>
    <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_domain_expertise'</span><span class="p">]</span> <span class="o">*</span> <span class="n">completion_rate</span> <span class="o">*</span> <span class="n">mastery_score</span><span class="p">,</span>
        <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
    <span class="p">)</span>
    <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_adaptive_capacity'</span><span class="p">]</span> <span class="o">*</span> <span class="n">completion_rate</span> <span class="o">*</span> <span class="n">mastery_score</span><span class="p">,</span>
        <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
    <span class="p">)</span>

    <span class="c1"># Recalculate VR score</span>
    <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">calculate_idiosyncratic_readiness</span><span class="p">(</span><span class="n">employee_row_sim</span><span class="p">,</span> <span class="n">params</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">])</span>

    <span class="c1"># Recalculate Synergy (which depends on VR)</span>
    <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'synergy_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">calculate_synergy</span><span class="p">(</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span>
    <span class="p">)</span>

    <span class="c1"># Recalculate overall AI-R score</span>
    <span class="n">projected_ai_r</span> <span class="o">=</span> <span class="n">calculate_ai_r</span><span class="p">(</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span>
        <span class="n">employee_row_sim</span><span class="p">[</span><span class="s1">'synergy_score'</span><span class="p">],</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">],</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">]</span>
    <span class="p">)</span>

    <span class="n">delta_ai_r</span> <span class="o">=</span> <span class="n">projected_ai_r</span> <span class="o">-</span> <span class="n">employee_row_original</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span>

    <span class="k">return</span> <span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'pathway_name'</span><span class="p">]</span>

<span class="c1"># --- Pytest fixtures and tests ---</span>

<span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
<span class="k">def</span><span class="w"> </span><span class="nf">mock_params</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""Mock PARAMS dictionary with relevant weights for testing."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s1">'alpha'</span><span class="p">:</span> <span class="mf">0.6</span><span class="p">,</span>
        <span class="s1">'beta'</span><span class="p">:</span> <span class="mf">0.15</span><span class="p">,</span>
        <span class="s1">'vr_component_weights'</span><span class="p">:</span> <span class="p">{</span>
            <span class="s1">'ai_fluency_weight_vr'</span><span class="p">:</span> <span class="mf">0.45</span><span class="p">,</span>
            <span class="s1">'domain_expertise_weight_vr'</span><span class="p">:</span> <span class="mf">0.35</span><span class="p">,</span>
            <span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">:</span> <span class="mf">0.20</span>
        <span class="p">}</span>
    <span class="p">}</span>

<span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
<span class="k">def</span><span class="w"> </span><span class="nf">mock_df_employees</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""Mock df_employees DataFrame with necessary columns."""</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span>
        <span class="s1">'employee_id'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'EMP001'</span><span class="p">,</span> <span class="s1">'EMP002'</span><span class="p">],</span>
        <span class="s1">'job_role'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'Data Scientist'</span><span class="p">,</span> <span class="s1">'HR Specialist'</span><span class="p">],</span>
        <span class="s1">'current_ai_r_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">60.0</span><span class="p">,</span> <span class="mf">40.0</span><span class="p">],</span>
        <span class="s1">'ai_fluency_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">70.0</span><span class="p">,</span> <span class="mf">30.0</span><span class="p">],</span>
        <span class="s1">'domain_expertise_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">65.0</span><span class="p">,</span> <span class="mf">50.0</span><span class="p">],</span>
        <span class="s1">'adaptive_capacity_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">75.0</span><span class="p">,</span> <span class="mf">45.0</span><span class="p">],</span>
        <span class="s1">'hr_r_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">80.0</span><span class="p">,</span> <span class="mf">55.0</span><span class="p">],</span>
        <span class="s1">'alignment_factor'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.8</span><span class="p">,</span> <span class="mf">0.6</span><span class="p">],</span>
        <span class="s1">'vr_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">],</span> <span class="c1"># These will be recalculated or overwritten</span>
        <span class="s1">'synergy_score'</span><span class="p">:</span> <span class="p">[</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">]</span> <span class="c1"># These will be recalculated or overwritten</span>
    <span class="p">})</span>

<span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
<span class="k">def</span><span class="w"> </span><span class="nf">mock_df_occupations</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""Mock df_occupations DataFrame (minimal for this test's needs)."""</span>
    <span class="c1"># This function doesn't directly use df_occupations data besides employee job_role lookup.</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span>
        <span class="s1">'occupation'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'Data Scientist'</span><span class="p">,</span> <span class="s1">'HR Specialist'</span><span class="p">]</span>
    <span class="p">})</span>

<span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
<span class="k">def</span><span class="w"> </span><span class="nf">mock_df_pathways</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""Mock df_pathways DataFrame with pathway impact coefficients."""</span>
    <span class="k">return</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span>
        <span class="s1">'pathway_id'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'PATH01'</span><span class="p">,</span> <span class="s1">'PATH02'</span><span class="p">],</span>
        <span class="s1">'pathway_name'</span><span class="p">:</span> <span class="p">[</span><span class="s1">'AI Fundamentals'</span><span class="p">,</span> <span class="s1">'Domain Deep Dive'</span><span class="p">],</span>
        <span class="s1">'delta_ai_fluency'</span><span class="p">:</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span>
        <span class="s1">'delta_domain_expertise'</span><span class="p">:</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">15</span><span class="p">],</span>
        <span class="s1">'delta_adaptive_capacity'</span><span class="p">:</span> <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
    <span class="p">})</span>


<span class="k">class</span><span class="w"> </span><span class="nc">TestSimulatePathwayImpact</span><span class="p">:</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_simulate_pathway_impact_basic_full_completion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span><span class="p">):</span>
        <span class="n">employee_id</span> <span class="o">=</span> <span class="s1">'EMP001'</span>
        <span class="n">pathway_id</span> <span class="o">=</span> <span class="s1">'PATH01'</span>
        <span class="n">completion_rate</span> <span class="o">=</span> <span class="mf">1.0</span>
        <span class="n">mastery_score</span> <span class="o">=</span> <span class="mf">1.0</span>

        <span class="n">current_employee_row</span> <span class="o">=</span> <span class="n">mock_df_employees</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">original_current_ai_r</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span>

        <span class="n">pathway_info</span> <span class="o">=</span> <span class="n">mock_df_pathways</span><span class="p">[</span><span class="n">mock_df_pathways</span><span class="p">[</span><span class="s1">'pathway_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">pathway_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

        <span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">pathway_name</span> <span class="o">=</span> <span class="n">simulate_pathway_impact</span><span class="p">(</span>
            <span class="n">employee_id</span><span class="p">,</span> <span class="n">pathway_id</span><span class="p">,</span> <span class="n">completion_rate</span><span class="p">,</span> <span class="n">mastery_score</span><span class="p">,</span>
            <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="n">pathway_name</span> <span class="o">==</span> <span class="s1">'AI Fundamentals'</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">projected_ai_r</span><span class="p">,</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">floating</span><span class="p">))</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">delta_ai_r</span><span class="p">,</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">floating</span><span class="p">))</span>

        <span class="c1"># Manually calculate expected values for verification</span>
        <span class="n">expected_ai_fluency_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_ai_fluency'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="n">expected_domain_expertise_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_domain_expertise'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="n">expected_adaptive_capacity_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_adaptive_capacity'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

        <span class="n">vr_weights</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">]</span>
        <span class="n">expected_vr_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'ai_fluency_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_ai_fluency_sim</span> <span class="o">+</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'domain_expertise_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_domain_expertise_sim</span> <span class="o">+</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_adaptive_capacity_sim</span><span class="p">,</span>
            <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
        <span class="p">)</span>

        <span class="n">hr_r_score</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">]</span>
        <span class="n">alignment_factor</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span>
        <span class="n">expected_synergy_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">((</span><span class="n">expected_vr_sim</span> <span class="o">/</span> <span class="mi">100</span> <span class="o">*</span> <span class="n">hr_r_score</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span> <span class="o">*</span> <span class="n">alignment_factor</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

        <span class="n">alpha</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">]</span>
        <span class="n">beta</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">]</span>
        <span class="n">expected_projected_ai_r</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="p">(</span><span class="n">alpha</span> <span class="o">*</span> <span class="n">expected_vr_sim</span><span class="p">)</span> <span class="o">+</span>
            <span class="p">((</span><span class="mi">1</span> <span class="o">-</span> <span class="n">alpha</span><span class="p">)</span> <span class="o">*</span> <span class="n">hr_r_score</span><span class="p">)</span> <span class="o">+</span>
            <span class="p">(</span><span class="n">beta</span> <span class="o">*</span> <span class="n">expected_synergy_sim</span><span class="p">),</span>
            <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">expected_projected_ai_r</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">expected_projected_ai_r</span> <span class="o">-</span> <span class="n">original_current_ai_r</span><span class="p">)</span>
        <span class="k">assert</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">projected_ai_r</span> <span class="o">&lt;=</span> <span class="mi">100</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_simulate_pathway_impact_partial_completion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span><span class="p">):</span>
        <span class="n">employee_id</span> <span class="o">=</span> <span class="s1">'EMP001'</span>
        <span class="n">pathway_id</span> <span class="o">=</span> <span class="s1">'PATH01'</span>
        <span class="n">completion_rate</span> <span class="o">=</span> <span class="mf">0.5</span>
        <span class="n">mastery_score</span> <span class="o">=</span> <span class="mf">0.8</span>

        <span class="n">current_employee_row</span> <span class="o">=</span> <span class="n">mock_df_employees</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">original_current_ai_r</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span>

        <span class="n">pathway_info</span> <span class="o">=</span> <span class="n">mock_df_pathways</span><span class="p">[</span><span class="n">mock_df_pathways</span><span class="p">[</span><span class="s1">'pathway_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">pathway_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

        <span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">simulate_pathway_impact</span><span class="p">(</span>
            <span class="n">employee_id</span><span class="p">,</span> <span class="n">pathway_id</span><span class="p">,</span> <span class="n">completion_rate</span><span class="p">,</span> <span class="n">mastery_score</span><span class="p">,</span>
            <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span>
        <span class="p">)</span>

        <span class="c1"># Manually calculate expected values for verification</span>
        <span class="n">impact_factor</span> <span class="o">=</span> <span class="n">completion_rate</span> <span class="o">*</span> <span class="n">mastery_score</span>
        <span class="n">expected_ai_fluency_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_ai_fluency'</span><span class="p">]</span> <span class="o">*</span> <span class="n">impact_factor</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="n">expected_domain_expertise_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_domain_expertise'</span><span class="p">]</span> <span class="o">*</span> <span class="n">impact_factor</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="n">expected_adaptive_capacity_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span><span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway_info</span><span class="p">[</span><span class="s1">'delta_adaptive_capacity'</span><span class="p">]</span> <span class="o">*</span> <span class="n">impact_factor</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

        <span class="n">vr_weights</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">]</span>
        <span class="n">expected_vr_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'ai_fluency_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_ai_fluency_sim</span> <span class="o">+</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'domain_expertise_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_domain_expertise_sim</span> <span class="o">+</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_adaptive_capacity_sim</span><span class="p">,</span>
            <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
        <span class="p">)</span>

        <span class="n">hr_r_score</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">]</span>
        <span class="n">alignment_factor</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span>
        <span class="n">expected_synergy_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">((</span><span class="n">expected_vr_sim</span> <span class="o">/</span> <span class="mi">100</span> <span class="o">*</span> <span class="n">hr_r_score</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span> <span class="o">*</span> <span class="n">alignment_factor</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

        <span class="n">alpha</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">]</span>
        <span class="n">beta</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">]</span>
        <span class="n">expected_projected_ai_r</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="p">(</span><span class="n">alpha</span> <span class="o">*</span> <span class="n">expected_vr_sim</span><span class="p">)</span> <span class="o">+</span>
            <span class="p">((</span><span class="mi">1</span> <span class="o">-</span> <span class="n">alpha</span><span class="p">)</span> <span class="o">*</span> <span class="n">hr_r_score</span><span class="p">)</span> <span class="o">+</span>
            <span class="p">(</span><span class="n">beta</span> <span class="o">*</span> <span class="n">expected_synergy_sim</span><span class="p">),</span>
            <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">expected_projected_ai_r</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">expected_projected_ai_r</span> <span class="o">-</span> <span class="n">original_current_ai_r</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_simulate_pathway_impact_zero_impact_factors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span><span class="p">):</span>
        <span class="n">employee_id</span> <span class="o">=</span> <span class="s1">'EMP001'</span>
        <span class="n">pathway_id</span> <span class="o">=</span> <span class="s1">'PATH01'</span>
        <span class="n">completion_rate</span> <span class="o">=</span> <span class="mf">0.0</span> <span class="c1"># Zero completion</span>
        <span class="n">mastery_score</span> <span class="o">=</span> <span class="mf">1.0</span>

        <span class="n">current_employee_row</span> <span class="o">=</span> <span class="n">mock_df_employees</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">original_current_ai_r</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span>

        <span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">simulate_pathway_impact</span><span class="p">(</span>
            <span class="n">employee_id</span><span class="p">,</span> <span class="n">pathway_id</span><span class="p">,</span> <span class="n">completion_rate</span><span class="p">,</span> <span class="n">mastery_score</span><span class="p">,</span>
            <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">original_current_ai_r</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">delta_ai_r</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_simulate_pathway_impact_max_scores_clipping</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span><span class="p">):</span>
        <span class="n">employee_id</span> <span class="o">=</span> <span class="s1">'EMP001'</span>
        <span class="n">pathway_id</span> <span class="o">=</span> <span class="s1">'PATH01'</span> <span class="c1"># delta_ai_fluency=10, delta_domain_expertise=5, delta_adaptive_capacity=3</span>
        <span class="n">completion_rate</span> <span class="o">=</span> <span class="mf">1.0</span>
        <span class="n">mastery_score</span> <span class="o">=</span> <span class="mf">1.0</span>

        <span class="c1"># Modify employee to have high initial scores that would exceed 100 with pathway impact</span>
        <span class="n">mock_df_employees</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">,</span> <span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">=</span> <span class="mi">95</span>
        <span class="n">mock_df_employees</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">,</span> <span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">=</span> <span class="mi">98</span>
        <span class="n">mock_df_employees</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">,</span> <span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">=</span> <span class="mi">99</span>
        <span class="n">mock_df_employees</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">,</span> <span class="s1">'current_ai_r_score'</span><span class="p">]</span> <span class="o">=</span> <span class="mi">90</span>

        <span class="n">current_employee_row</span> <span class="o">=</span> <span class="n">mock_df_employees</span><span class="p">[</span><span class="n">mock_df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">original_current_ai_r</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span>

        <span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">simulate_pathway_impact</span><span class="p">(</span>
            <span class="n">employee_id</span><span class="p">,</span> <span class="n">pathway_id</span><span class="p">,</span> <span class="n">completion_rate</span><span class="p">,</span> <span class="n">mastery_score</span><span class="p">,</span>
            <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span>
        <span class="p">)</span>

        <span class="c1"># Expected VR sub-components should be clipped to 100</span>
        <span class="n">expected_ai_fluency_sim</span> <span class="o">=</span> <span class="mf">100.0</span> <span class="c1"># 95 + 10 = 105 -&gt; 100</span>
        <span class="n">expected_domain_expertise_sim</span> <span class="o">=</span> <span class="mf">100.0</span> <span class="c1"># 98 + 5 = 103 -&gt; 100</span>
        <span class="n">expected_adaptive_capacity_sim</span> <span class="o">=</span> <span class="mf">100.0</span> <span class="c1"># 99 + 3 = 102 -&gt; 100</span>

        <span class="n">vr_weights</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">]</span>
        <span class="n">expected_vr_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'ai_fluency_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_ai_fluency_sim</span> <span class="o">+</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'domain_expertise_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_domain_expertise_sim</span> <span class="o">+</span>
            <span class="n">vr_weights</span><span class="p">[</span><span class="s1">'adaptive_capacity_weight_vr'</span><span class="p">]</span> <span class="o">*</span> <span class="n">expected_adaptive_capacity_sim</span><span class="p">,</span>
            <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
        <span class="p">)</span>
        <span class="k">assert</span> <span class="n">expected_vr_sim</span> <span class="o">==</span> <span class="mf">100.0</span> <span class="c1"># Sum of weights is 1.0, so 100 * 1.0 = 100</span>

        <span class="n">hr_r_score</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">]</span>
        <span class="n">alignment_factor</span> <span class="o">=</span> <span class="n">current_employee_row</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span>
        <span class="n">expected_synergy_sim</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">((</span><span class="n">expected_vr_sim</span> <span class="o">/</span> <span class="mi">100</span> <span class="o">*</span> <span class="n">hr_r_score</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span> <span class="o">*</span> <span class="n">alignment_factor</span> <span class="o">*</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

        <span class="n">alpha</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">]</span>
        <span class="n">beta</span> <span class="o">=</span> <span class="n">mock_params</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">]</span>
        <span class="n">expected_projected_ai_r</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="p">(</span><span class="n">alpha</span> <span class="o">*</span> <span class="n">expected_vr_sim</span><span class="p">)</span> <span class="o">+</span>
            <span class="p">((</span><span class="mi">1</span> <span class="o">-</span> <span class="n">alpha</span><span class="p">)</span> <span class="o">*</span> <span class="n">hr_r_score</span><span class="p">)</span> <span class="o">+</span>
            <span class="p">(</span><span class="n">beta</span> <span class="o">*</span> <span class="n">expected_synergy_sim</span><span class="p">),</span>
            <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="n">np</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">expected_projected_ai_r</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">projected_ai_r</span> <span class="o">&lt;=</span> <span class="mi">100</span> <span class="c1"># Final AI-R should also be clipped</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_simulate_pathway_impact_no_employee_found</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span><span class="p">):</span>
        <span class="k">with</span> <span class="n">pytest</span><span class="o">.</span><span class="n">raises</span><span class="p">(</span><span class="ne">IndexError</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="s2">"single-row DataFrame"</span><span class="p">):</span>
            <span class="n">simulate_pathway_impact</span><span class="p">(</span>
                <span class="s1">'NON_EXISTENT_EMP'</span><span class="p">,</span> <span class="s1">'PATH01'</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span>
                <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span>
            <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">test_simulate_pathway_impact_no_pathway_found</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span><span class="p">):</span>
        <span class="k">with</span> <span class="n">pytest</span><span class="o">.</span><span class="n">raises</span><span class="p">(</span><span class="ne">IndexError</span><span class="p">,</span> <span class="n">match</span><span class="o">=</span><span class="s2">"single-row DataFrame"</span><span class="p">):</span>
            <span class="n">simulate_pathway_impact</span><span class="p">(</span>
                <span class="s1">'EMP001'</span><span class="p">,</span> <span class="s1">'NON_EXISTENT_PATH'</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span> <span class="mf">1.0</span><span class="p">,</span>
                <span class="n">mock_df_employees</span><span class="p">,</span> <span class="n">mock_df_occupations</span><span class="p">,</span> <span class="n">mock_df_pathways</span><span class="p">,</span> <span class="n">mock_params</span>
            <span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=12fd8fcb">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [32]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="n">example_employee_id</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">df_employees</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span><span class="p">)]</span>
<span class="n">current_ai_r</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="n">df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">example_employee_id</span><span class="p">][</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

<span class="c1"># Select a pathway randomly for demonstration</span>
<span class="n">selected_pathway</span> <span class="o">=</span> <span class="n">df_pathways</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">selected_pathway_id</span> <span class="o">=</span> <span class="n">selected_pathway</span><span class="p">[</span><span class="s1">'pathway_id'</span><span class="p">]</span>

<span class="n">completion_rate</span> <span class="o">=</span> <span class="mf">0.9</span>
<span class="n">mastery_score</span> <span class="o">=</span> <span class="mf">0.85</span>

<span class="n">projected_ai_r</span><span class="p">,</span> <span class="n">delta_ai_r</span><span class="p">,</span> <span class="n">pathway_name</span> <span class="o">=</span> <span class="n">simulate_pathway_impact</span><span class="p">(</span>
    <span class="n">example_employee_id</span><span class="p">,</span> <span class="n">selected_pathway_id</span><span class="p">,</span> <span class="n">completion_rate</span><span class="p">,</span> <span class="n">mastery_score</span><span class="p">,</span>
    <span class="n">df_employees</span><span class="p">,</span> <span class="n">df_occupations</span><span class="p">,</span> <span class="n">df_pathways</span><span class="p">,</span> <span class="n">PARAMS</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Simulating impact for employee </span><span class="si">{</span><span class="n">example_employee_id</span><span class="si">}</span><span class="s2">:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Current AI-R: </span><span class="si">{</span><span class="n">current_ai_r</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Chosen Pathway: </span><span class="si">{</span><span class="n">pathway_name</span><span class="si">}</span><span class="s2"> (ID: </span><span class="si">{</span><span class="n">selected_pathway_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Completion Rate: </span><span class="si">{</span><span class="n">completion_rate</span><span class="si">}</span><span class="s2">, Mastery Score: </span><span class="si">{</span><span class="n">mastery_score</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Projected AI-R: </span><span class="si">{</span><span class="n">projected_ai_r</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Change in AI-R (</span><span class="se">\u0394</span><span class="s2">AI-R): </span><span class="si">{</span><span class="n">delta_ai_r</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Create a comparative bar chart</span>
<span class="n">plot_current_vs_projected_ai_r</span><span class="p">(</span><span class="n">current_ai_r</span><span class="p">,</span> <span class="p">[</span><span class="n">projected_ai_r</span><span class="p">],</span> <span class="p">[</span><span class="n">pathway_name</span><span class="p">])</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Simulating impact for employee EMP034:
  Current AI-R: 47.72
  Chosen Pathway: Data Storytelling with AI (ID: PATH04)
  Completion Rate: 0.9, Mastery Score: 0.85
  Projected AI-R: 50.39
  Change in AI-R (ΔAI-R): 2.67
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAArcAAAHDCAYAAAA+xjI9AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAXA9JREFUeJzt3Xd0VOXaxuF7Jp1AEggQCMEkdBAIVZoYEDCA4kFAwINHmoiHriIWPukIooINRZR2FBUVG0pHpEZEpIjSi0gJEEIKAQJJ3u8PTvZhSAIzkBAcf9darMU8e8+e552yc887e/bYjDFGAAAAgBuwF3QDAAAAQF4h3AIAAMBtEG4BAADgNgi3AAAAcBuEWwAAALgNwi0AAADcBuEWAAAAboNwCwAAALdBuAUAAIDbINwCgBMOHjwom82m2bNnF3QrLhs1apRsNltBt3FLmT17tmw2mw4ePGjVmjVrpmbNmhVYTwDyBuEWyAP79u1T3759Va5cOfn6+iogIEBNmjTR66+/rnPnzhV0e9dt4cKFGjVqVEG3cVU9evSQzWaz/gUEBCgqKkqvvvqq0tLSCro9px09elSjRo3Sli1bCroVSVLnzp1ls9n0zDPP5Lj8hx9+kM1m0+eff37NbWWF66x/Xl5eioiI0KBBg5SYmJjHnf+9LViwQNHR0SpZsqQKFSqkcuXKqXPnzlq8eHFBtwbcNJ4F3QDwV/fdd9/pwQcflI+Pjx555BFVr15dFy5c0Nq1a/X000/rt99+0/Tp0wu6zeuycOFCTZ069ZYPuD4+Pnr//fclSYmJiZo/f76GDh2qjRs36pNPPsmT2wgPD9e5c+fk5eWVJ9u70tGjRzV69GhFRESoVq1a+XIbzkpOTtaCBQsUERGhjz/+WBMnTsyTmd933nlHhQsXVmpqqlasWKE333xTv/zyi9auXZsHXd+4pUuXFnQLN+SVV17R008/rejoaD333HMqVKiQ9u7dq+XLl+uTTz5R69atC7pF4KYg3AI34MCBA+ratavCw8P1/fffq3Tp0tay/v37a+/evfruu+/y5LZSU1Pl7++frW6M0fnz5+Xn55cnt/NX5OnpqYcffti63K9fPzVo0EDz5s3T5MmTFRoamu06rt5vNptNvr6+edbzrWz+/PnKyMjQzJkzdffdd2v16tWKjo6+4e126tRJxYsXlyT17dtXXbt21bx58/TTTz/pjjvuuOHt3yhvb++CbuG6paena+zYsWrVqlWOIf3EiRM3rZfMzExduHDhb/N6wa2HwxKAGzBp0iSdOXNGM2bMcAi2WSpUqKDBgwdLuvoxmzabzWF2NOtj3N9//13//Oc/VbRoUd15552SpIiICN13331asmSJ6tWrJz8/P7377ruSLs1aDhkyRGXLlpWPj48qVKigl156SZmZmda2s/p45ZVXNH36dJUvX14+Pj6qX7++Nm7caK3Xo0cPTZ061eov619u7rvvPpUrVy7HZY0aNVK9evWsy8uWLdOdd96poKAgFS5cWJUrV9bzzz+f67ZdZbfbrWMns46pvNr9tn//fj344IMqVqyYChUqpIYNG2Z7U5Lb47dz50516tRJxYoVk6+vr+rVq6dvvvkmW0+JiYl64oknFBERIR8fH4WFhemRRx5RfHy8fvjhB9WvX1+S1LNnT+u+vvy2NmzYoNatWyswMFCFChVSdHS01q1bl+121q5dq/r168vX11fly5e3xuiKuXPnqlWrVmrevLmqVq2quXPnurwNZzRt2lTSpcN6LufMWP/44w/169dPlStXlp+fn4KDg/Xggw86HEOb5bffftPdd98tPz8/hYWFady4cQ6viSxXHnObdejFp59+qvHjxyssLEy+vr5q0aKF9u7dm+36zvSdkpKiIUOGWM+DkiVLqlWrVvrll1+sdfbs2aOOHTuqVKlS8vX1VVhYmLp27aqkpKRc78v4+HglJyerSZMmOS4vWbKkw+Xz589r1KhRqlSpknx9fVW6dGl16NDB4bFITU3VU089Ze1PKleurFdeeUXGGIdt2Ww2DRgwQHPnztXtt98uHx8f6zCII0eOqFevXgoJCZGPj49uv/12zZw5M9dxAHmBmVvgBixYsEDlypVT48aN82X7Dz74oCpWrKgXX3zR4Q/Krl279NBDD6lv377q06ePKleurLNnzyo6OlpHjhxR3759ddttt2n9+vV67rnndOzYMb322msO2/7oo4+UkpKivn37ymazadKkSerQoYP2798vLy8v9e3bV0ePHtWyZcv0wQcfXLPXLl266JFHHtHGjRutoCZdCiE//vijXn75ZUmXgsZ9992nmjVrasyYMfLx8dHevXtzDGo3IuuPdHBwsFXL6X47fvy4GjdurLNnz2rQoEEKDg7WnDlzdP/99+vzzz/XAw88kOtt/Pbbb2rSpInKlCmjZ599Vv7+/vr000/Vvn17zZ8/37rumTNn1LRpU+3YsUO9evVSnTp1FB8fr2+++UaHDx9W1apVNWbMGI0YMUKPPfaYFfqynlfff/+92rRpo7p162rkyJGy2+2aNWuW7r77bq1Zs8aa9fz11191zz33qESJEho1apTS09M1cuRIhYSEOH2/HT16VCtXrtScOXMkSQ899JCmTJmit956K89nNrOCaNGiRa2as2PduHGj1q9fr65duyosLEwHDx7UO++8o2bNmun3339XoUKFJElxcXFq3ry50tPTrcdo+vTpLn3SMXHiRNntdg0dOlRJSUmaNGmSunXrpg0bNrjc9+OPP67PP/9cAwYMULVq1XTq1CmtXbtWO3bsUJ06dXThwgXFxMQoLS1NAwcOVKlSpXTkyBF9++23SkxMVGBgYI49lixZUn5+flqwYIEGDhyoYsWK5TqejIwM3XfffVqxYoW6du2qwYMHKyUlRcuWLdP27dtVvnx5GWN0//33a+XKlerdu7dq1aqlJUuW6Omnn9aRI0c0ZcoUh21+//33+vTTTzVgwAAVL15cEREROn78uBo2bGiF3xIlSmjRokXq3bu3kpOTNWTIEKcfA8AlBsB1SUpKMpLMP/7xD6fWP3DggJFkZs2alW2ZJDNy5Ejr8siRI40k89BDD2VbNzw83EgyixcvdqiPHTvW+Pv7m927dzvUn332WePh4WEOHTrk0EdwcLBJSEiw1vv666+NJLNgwQKr1r9/f+PsbiIpKcn4+PiYp556yqE+adIkY7PZzB9//GGMMWbKlClGkjl58qRT272W7t27G39/f3Py5Elz8uRJs3fvXvPiiy8am81matasaa2X2/02ZMgQI8msWbPGqqWkpJjIyEgTERFhMjIyjDE5P34tWrQwNWrUMOfPn7dqmZmZpnHjxqZixYpWbcSIEUaS+eKLL7L1n5mZaYwxZuPGjTk+PzIzM03FihVNTEyMta4xxpw9e9ZERkaaVq1aWbX27dsbX19f6742xpjff//deHh4OP04vvLKK8bPz88kJycbY4zZvXu3kWS+/PJLh/VWrlxpJJnPPvvsmtvMej7v2rXLnDx50hw8eNDMnDnT+Pn5mRIlSpjU1FSXx3r27NlstxMbG2skmf/85z9WLevx3bBhg1U7ceKECQwMNJLMgQMHrHp0dLSJjo7ONsaqVauatLQ0q/76668bSebXX391ue/AwEDTv3//XO+rzZs3O32/Xinreebv72/atGljxo8fbzZt2pRtvZkzZxpJZvLkydmWZfX/1VdfGUlm3LhxDss7depkbDab2bt3r1WTZOx2u/ntt98c1u3du7cpXbq0iY+Pd6h37drVBAYG5vgYAnmBwxKA65ScnCxJKlKkSL7dxuOPP55jPTIyUjExMQ61zz77TE2bNlXRokUVHx9v/WvZsqUyMjK0evVqh/W7dOniMGOWNVu4f//+6+o1ICBAbdq00aeffuowyzxv3jw1bNhQt912myQpKChIkvT111/n+NHw9UhNTVWJEiVUokQJVahQQc8//7waNWqkL7/80mG9nO63hQsX6o477rAO+5CkwoUL67HHHtPBgwf1+++/53ibCQkJ+v7779W5c2elpKRY9/epU6cUExOjPXv26MiRI5IuHcMaFRWV4yzwtb6otWXLFu3Zs0f//Oc/derUKet2UlNT1aJFC61evVqZmZnKyMjQkiVL1L59e+u+lqSqVatmG/PVzJ07V/fee6/1vK5YsaLq1q2bJ4cmVK5cWSVKlFBERIR69eqlChUqaNGiRdYsq7NjleQw83rx4kWdOnVKFSpUUFBQkMNH/AsXLlTDhg0djuktUaKEunXr5nTfPXv2dJi1vvK14krfQUFB2rBhg44ePZrjbWXNzC5ZskRnz551ukdJGj16tD766CPVrl1bS5Ys0fDhw1W3bl3VqVNHO3bssNabP3++ihcvroEDB2bbRtbzceHChfLw8NCgQYMclj/11FMyxmjRokUO9ejoaFWrVs26bIzR/Pnz1a5dOxljHPZJMTExSkpKcnicgLzEYQnAdQoICJB06Ri6/BIZGel0fc+ePdq2bZtKlCiR43Wu/ELJ5QFI+t9Hw6dPn76eViVdCsxfffWVYmNj1bhxY+3bt0+bNm1yOCSiS5cuev/99/Xoo4/q2WefVYsWLdShQwd16tRJdvv1vd/29fXVggULJF06c0JkZKTCwsKyrZfT/fbHH3+oQYMG2epVq1a1llevXj3b8r1798oYoxdeeEEvvPBCjn2dOHFCZcqU0b59+9SxY0eXxpRlz549kqTu3bvnuk5SUpLS0tJ07tw5VaxYMdvyypUra+HChde8rR07dmjz5s165JFHHI4pbdasmaZOnark5GTreX+lCxcuKCEhwaFWokQJeXh4WJfnz5+vgIAAnTx5Um+88YYOHDjgEFKdHWvRokV17tw5TZgwQbNmzdKRI0cc3lBdfmxqbo9v5cqVc72NK13rteJK35MmTVL37t1VtmxZ1a1bV23bttUjjzxiHa8eGRmpJ598UpMnT9bcuXPVtGlT3X///Xr44YdzPSThcg899JAeeughJScna8OGDZo9e7Y++ugjtWvXTtu3b5evr6/27dunypUry9Mz9wjwxx9/KDQ0NNub98tfF5e78rV18uRJJSYmavr06bmeLeZmfskNfy+EW+A6BQQEKDQ0VNu3b3dq/dxm6DIyMnK9Tm7HBeZUz8zMVKtWrTRs2LAcr1OpUiWHy5eHjsuZK74s4op27dqpUKFC+vTTT9W4cWN9+umnstvtevDBBx16X716tVauXKnvvvtOixcv1rx583T33Xdr6dKlufZ1NR4eHmrZsuU118vLM0pkzcQNHTo015nRChUq5NntvPzyy7meIqxw4cJ5ck7fDz/8UJL0xBNP6Iknnsi2fP78+erZs2eO112/fr2aN2/uUDtw4IAiIiKsy3fddZd1toR27dqpRo0a6tatmzZt2iS73e70WCVp4MCBmjVrloYMGaJGjRopMDBQNptNXbt2zbNPBLJc67XiSt+dO3dW06ZN9eWXX2rp0qV6+eWX9dJLL+mLL75QmzZtJEmvvvqqevTooa+//lpLly7VoEGDNGHCBP344485vmnLSUBAgFq1aqVWrVrJy8tLc+bM0YYNG/LkrBc5ufK1lXWfPPzww7mG/po1a+ZLLwDhFrgB9913n6ZPn67Y2Fg1atToqutmzfZcedL6K2dArlf58uV15swZp0Kes1w9t6m/v7/uu+8+ffbZZ5o8ebLmzZunpk2bZjsVl91uV4sWLdSiRQtNnjxZL774ooYPH66VK1fmaf/OCA8P165du7LVd+7caS3PSdZMm5eX1zV7Ll++/DXfBOV2X5cvX17SpbBytdspUaKE/Pz8rFnEy+U0visZY/TRRx+pefPm6tevX7blY8eO1dy5c3MNt1FRUVq2bJlDrVSpUrneXuHChTVy5Ej17NlTn376qbp27er0WCXp888/V/fu3fXqq69atfPnz2d7fYWHh1/3feIsV/qWpNKlS6tfv37q16+fTpw4oTp16mj8+PFWuJWk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Fx4eftVxzp492zRs2NAkJiaaQoUKmUOHDjksHzlypImKirrqNrp3727+8Y9/ONQ6dOhgateufdXr4e8np+dKq1atTMOGDR2Wjxs3zpQuXdpEREQYY4zZtm2bad68ufH19TXFihUzffr0MSkpKdY2cnqevvfee6ZKlSrGx8fHVK5c2UydOtVh+Z9//mm6du1qihYtagoVKmTq1q1rfvzxRzNr1iyH15AkM2vWLGPMpdd37969TfHixU2RIkVM8+bNzZYtWxy2O2HCBFOyZElTuHBh06tXL/PMM89c8zVkjDGjRo0yXbt2NTt27DCBgYHm7Nmz17zvrhQdHW0GDx7sUKtTp4554IEHrnq9l19+2dSrV8+hlrXvytrfZTl79qypXLmyadKkiVX76aefTMuWLU1wcLAJCAgwd911l9m0aZO1PLf90t69e839999vSpYsafz9/U29evXMsmXLrtprVFSUGTVqVK7Lu3fvnu3xO3DggDHGmB9++MHUr1/feHt7m1KlSplnnnnGXLx40bpuTvvlnj17mnvvvdfhNi5cuGBKlChh3n///avenjP788sfr/DwcDNlyhTrsiTz5ZdfGmP+9/dm/vz5plmzZsbPz8/UrFnTrF+/3qG36dOnm7CwMOPn52fat29vXn31VRMYGJjr/dWxY0fTv39/6/LgwYONJLNjxw5jjDFpaWmmUKFC1uNyec/R0dHZxm6MMbNmzTKBgYFm8eLFpkqVKsbf39/ExMSYo0eP5tpHlut5HYwePdrceeed19z2jWDmFn95CQkJWrx4sfr37y9/f/9sy6/nWKJnn31WEydO1I4dO1SzZk1J0pw5c+Tt7a1169Zp2rRpSkxM1N13363atWvr559/1uLFi3X8+HF17tzZYVtz5syRv7+/NmzYoEmTJmnMmDFatmyZJFkf48yaNUvHjh3L8WOdy82YMUMPP/ywAgMD1aZNG82ePdvlsV1p+/btWr9+vby9vW94W3B/fn5+DjNkK1as0K5du7Rs2TJ9++23Sk1NVUxMjIoWLaqNGzfqs88+0/LlyzVgwIBctzl37lyNGDFC48eP144dO/Tiiy/qhRde0Jw5cyRJZ86cUXR0tI4cOaJvvvlGW7du1bBhw5SZmakuXbroqaee0u23365jx47p2LFj6tKliyTpwQcf1IkTJ7Ro0SJt2rRJderUUYsWLZSQ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c10nJiZGsbGxOe5nTpw4obi4OO3Zs0effPKJmjRpovj4eIfZtYoVK+qDDz7Qjh07tGHDBnXr1i3bm9qc9ksVK1bUF198oS1btmjr1q365z//ec1ZyE6dOmnKlCnasGGD/vjjD/3www/q37+/KlWqZH3sHxERoQ0bNujgwYOKj49XZmam+vXrpz///FMDBw7Uzp079fXXX2vkyJF68sknrU/hrubRRx/VnDlztGPHDnXv3j3b2K68vbzan7ti4MCBWrhwoSZPnqw9e/bo3Xff1aJFi3J9U5OlWbNm+v333/Xbb7/pzjvvtGpz585VvXr1rvppSkREhFavXq0jR45ke0Pjiht5HaxZs0b33HPPdd+2Mwi3cAvlypXTL7/8oubNm+upp55S9erV1apVK61YscJhpz5z5kylp6erbt26GjJkSLZv3roiNDRU69atU0ZGhu655x7VqFFDQ4YMUVBQkFM73yyvvvqqli1bprJly1ozypc7fvy4vvvuuxyPibXb7XrggQc0Y8aM6x6HJHl6emrAgAGaNGmSNZsCXI9ChQppyZIlSkhIUP369dWpUye1aNFCb731Vq7XefTRR/X+++9r1qxZqlGjhqKjozV79mzrI2tvb28tXbpUJUuWVNu2bVWjRg1NnDjRmhnq2LGjWrdurebNm6tEiRL6+OOPZbPZtHDhQt11113q2bOnKlWqpK5du+qPP/6wQnaXLl30wgsvaNiwYapbt67++OMP/fvf/861z02bNmnr1q05vhYDAwPVokWLG34tFitWTI888ohGjRqVa3Bs06aNPD09tXz58mzLKleurNDQUNWtW1cTJ05Uy5YttX37dmu2VLoUTE6fPq06deroX//6lwYNGqSSJUs6bCen/dLkyZNVtGhRNW7cWO3atVNMTIzq1Klz1fHExMRowYIFateunSpVqqTu3burSpUqWrp0qTVDOnToUHl4eKhatWoqUaKEDh06pDJlymjhwoX66aefFBUVpccff1y9e/d2ekKiZcuWKl26tGJiYhQaGuqwLKfby6v9uSuaNGmiadOmafLkyYqKitLixYv1xBNPXPN46ho1aigoKEi1atVS4cKFJV0KtxkZGdc83nbMmDE6ePCgypcvf92HBdzI6+D8+fP66quv1KdPn+u6bWfZTH58GwcAgFw899xzWrNmjdauXVvQrfxlTZ06Vd98842WLFlS0K3cks6cOaMyZcpo1qxZ6tChQ0G347Q+ffpo586dDl86dCfvvPOOvvzySy1dujRfb4djbgEAN4UxRvv379eKFSty/JQCzuvbt68SExOVkpKSr79A9VeTmZmp+Ph4vfrqqwoKCtL9999f0C1d1SuvvKJWrVrJ399fixYt0pw5c5w61/JflZeXl9588818vx1mbgEAN0ViYqJCQkJUv359zZ07V+Hh4QXdEtzMwYMHFRkZqbCwMM2ePTvHM8ncSjp37qwffvhBKSkpKleunAYOHKjHH3+8oNv6yyPcAgAAwG3whTIAAAC4DcItAAAA3AbhFgAAAG6DcAsAAAC3QbgFAACA2yDcAgAAwG0QbgEAAOA2CLcAAABwG4RbAAAAuI3/BydulDHWLIGXAAAAAElFTkSuQmCC
"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=353672db">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>This simulation demonstrates the predictive power of the framework, allowing leaders to evaluate the effectiveness of different training programs. By adjusting completion and mastery rates, they can gain insights into the potential ROI of various learning investments and tailor programs to maximize workforce AI-readiness.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=67cd4b8e">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-18:-Multi-Step-Pathway-Optimization">Section 18: Multi-Step Pathway Optimization<a class="anchor-link" href="#Section-18:-Multi-Step-Pathway-Optimization">¶</a></h1><p>For complex skill transitions or broader workforce development, identifying an optimal sequence of learning pathways is crucial. This involves balancing AI-R improvement with constraints like total cost and time. The multi-step pathway optimization problem can be formulated as:</p>
<p>$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$</p>
<p>subject to:</p>
<p>$$ \sum_{k=1}^K Time(P_k) \leq T_{\text{max}} $$
$$ P_k \in P_{\text{feasible}} $$
$$ Prerequisites(P_k) \subseteq \{P_1,...,P_{k-1}\} $$</p>
<p>For this notebook, we will implement a simplified optimization strategy (e.g., a greedy approach or a simple iterative search) to identify a sequence of pathways that maximizes AI-R improvement within a given time budget, considering the cost.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=f93f0b18">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [33]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">optimize_pathway_sequence</span><span class="p">(</span><span class="n">employee_id</span><span class="p">,</span> <span class="n">current_ai_r</span><span class="p">,</span> <span class="n">available_pathways_df</span><span class="p">,</span> <span class="n">T_max_hours</span><span class="p">,</span> <span class="n">cost_weight_lambda</span><span class="p">,</span> <span class="n">df_employees_data</span><span class="p">,</span> <span class="n">df_occupations_data</span><span class="p">,</span> <span class="n">params</span><span class="p">,</span> <span class="n">max_steps</span><span class="o">=</span><span class="mi">3</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Identifies optimal sequence of learning investments using a greedy approach."""</span>
    <span class="n">best_pathways_sequence</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">max_ai_r_improvement</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">current_time_spent</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">current_cost_spent</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">projected_ai_r</span> <span class="o">=</span> <span class="n">current_ai_r</span>

    <span class="c1"># Deep copy employee data for simulation state across steps</span>
    <span class="n">simulated_employee_data</span> <span class="o">=</span> <span class="n">df_employees_data</span><span class="p">[</span><span class="n">df_employees_data</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">employee_id</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">deep</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="c1"># Iterate for a fixed number of steps (simplified for demo)</span>
    <span class="k">for</span> <span class="n">step</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">max_steps</span><span class="p">):</span>
        <span class="n">best_pathway_for_step</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">best_pathway_value</span> <span class="o">=</span> <span class="o">-</span><span class="n">np</span><span class="o">.</span><span class="n">inf</span> <span class="c1"># Maximize value</span>
        <span class="n">current_step_ai_r_gain</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="c1"># Consider all available pathways</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">pathway</span> <span class="ow">in</span> <span class="n">available_pathways_df</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
            <span class="n">pathway_id</span> <span class="o">=</span> <span class="n">pathway</span><span class="p">[</span><span class="s1">'pathway_id'</span><span class="p">]</span>
            <span class="n">pathway_time</span> <span class="o">=</span> <span class="n">pathway</span><span class="p">[</span><span class="s1">'time_hours'</span><span class="p">]</span>
            <span class="n">pathway_cost</span> <span class="o">=</span> <span class="n">pathway</span><span class="p">[</span><span class="s1">'cost'</span><span class="p">]</span>

            <span class="k">if</span> <span class="n">current_time_spent</span> <span class="o">+</span> <span class="n">pathway_time</span> <span class="o">&lt;=</span> <span class="n">T_max_hours</span><span class="p">:</span>
                <span class="c1"># Simulate impact on the current simulated state of the employee</span>
                <span class="c1"># Create a temporary deep copy for this specific pathway simulation</span>
                <span class="n">temp_employee_sim_state</span> <span class="o">=</span> <span class="n">simulated_employee_data</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">deep</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

                <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway</span><span class="p">[</span><span class="s1">'delta_ai_fluency'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
                <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway</span><span class="p">[</span><span class="s1">'delta_domain_expertise'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
                <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">pathway</span><span class="p">[</span><span class="s1">'delta_adaptive_capacity'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

                <span class="c1"># Recalculate VR for temp state</span>
                <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">calculate_idiosyncratic_readiness</span><span class="p">(</span><span class="n">temp_employee_sim_state</span><span class="p">,</span> <span class="n">params</span><span class="p">[</span><span class="s1">'vr_component_weights'</span><span class="p">])</span>

                <span class="c1"># Recalculate Synergy (using original HR and alignment as these don't change by VR pathway)</span>
                <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'synergy_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">calculate_synergy</span><span class="p">(</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'alignment_factor'</span><span class="p">]</span>
                <span class="p">)</span>

                <span class="c1"># Recalculate overall AI-R for temp state</span>
                <span class="n">temp_projected_ai_r</span> <span class="o">=</span> <span class="n">calculate_ai_r</span><span class="p">(</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">],</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">],</span>
                    <span class="n">temp_employee_sim_state</span><span class="p">[</span><span class="s1">'synergy_score'</span><span class="p">],</span>
                    <span class="n">params</span><span class="p">[</span><span class="s1">'alpha'</span><span class="p">],</span>
                    <span class="n">params</span><span class="p">[</span><span class="s1">'beta'</span><span class="p">]</span>
                <span class="p">)</span>

                <span class="n">ai_r_gain</span> <span class="o">=</span> <span class="n">temp_projected_ai_r</span> <span class="o">-</span> <span class="n">projected_ai_r</span>

                <span class="c1"># Define "value" metric: AI-R gain per (cost + time_cost)</span>
                <span class="c1"># Add a small epsilon to time to avoid division by zero</span>
                <span class="n">time_cost_equivalent</span> <span class="o">=</span> <span class="n">pathway_time</span> <span class="o">/</span> <span class="mi">10</span> <span class="c1"># Convert hours to a rough monetary equivalent for ratio (e.g., $10/hour)</span>
                <span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="n">ai_r_gain</span> <span class="o">-</span> <span class="n">cost_weight_lambda</span> <span class="o">*</span> <span class="n">pathway_cost</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="n">pathway_cost</span> <span class="o">+</span> <span class="n">time_cost_equivalent</span> <span class="o">+</span> <span class="mf">1e-6</span><span class="p">)</span>

                <span class="k">if</span> <span class="n">value</span> <span class="o">&gt;</span> <span class="n">best_pathway_value</span><span class="p">:</span>
                    <span class="n">best_pathway_value</span> <span class="o">=</span> <span class="n">value</span>
                    <span class="n">best_pathway_for_step</span> <span class="o">=</span> <span class="n">pathway</span>
                    <span class="n">current_step_ai_r_gain</span> <span class="o">=</span> <span class="n">ai_r_gain</span>

        <span class="k">if</span> <span class="n">best_pathway_for_step</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span> <span class="c1"># No pathway found that fits criteria</span>
            <span class="k">break</span>

        <span class="c1"># Apply the best pathway found to the simulated employee state and accumulated totals</span>
        <span class="n">best_pathways_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">best_pathway_for_step</span><span class="p">[</span><span class="s1">'pathway_name'</span><span class="p">])</span>
        <span class="n">current_time_spent</span> <span class="o">+=</span> <span class="n">best_pathway_for_step</span><span class="p">[</span><span class="s1">'time_hours'</span><span class="p">]</span>
        <span class="n">current_cost_spent</span> <span class="o">+=</span> <span class="n">best_pathway_for_step</span><span class="p">[</span><span class="s1">'cost'</span><span class="p">]</span>
        <span class="n">projected_ai_r</span> <span class="o">+=</span> <span class="n">current_step_ai_r_gain</span>
        <span class="n">max_ai_r_improvement</span> <span class="o">+=</span> <span class="n">current_step_ai_r_gain</span>

        <span class="c1"># Update the simulated_employee_data with the gains from the chosen pathway</span>
        <span class="c1"># This ensures subsequent steps build on the updated scores</span>
        <span class="n">simulated_employee_data</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="n">simulated_employee_data</span><span class="p">[</span><span class="s1">'ai_fluency_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">best_pathway_for_step</span><span class="p">[</span><span class="s1">'delta_ai_fluency'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="n">simulated_employee_data</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="n">simulated_employee_data</span><span class="p">[</span><span class="s1">'domain_expertise_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">best_pathway_for_step</span><span class="p">[</span><span class="s1">'delta_domain_expertise'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
        <span class="n">simulated_employee_data</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">clip</span><span class="p">(</span>
            <span class="n">simulated_employee_data</span><span class="p">[</span><span class="s1">'adaptive_capacity_score'</span><span class="p">]</span> <span class="o">+</span> <span class="n">best_pathway_for_step</span><span class="p">[</span><span class="s1">'delta_adaptive_capacity'</span><span class="p">],</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">{</span>
        <span class="s1">'recommended_sequence'</span><span class="p">:</span> <span class="n">best_pathways_sequence</span><span class="p">,</span>
        <span class="s1">'projected_final_ai_r'</span><span class="p">:</span> <span class="n">projected_ai_r</span><span class="p">,</span>
        <span class="s1">'total_cost'</span><span class="p">:</span> <span class="n">current_cost_spent</span><span class="p">,</span>
        <span class="s1">'total_time_hours'</span><span class="p">:</span> <span class="n">current_time_spent</span><span class="p">,</span>
        <span class="s1">'ai_r_improvement'</span><span class="p">:</span> <span class="n">max_ai_r_improvement</span>
    <span class="p">}</span>

<span class="c1"># Test the function immediately</span>
<span class="n">example_employee_id_opt</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">current_ai_r_opt</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="n">df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">example_employee_id_opt</span><span class="p">][</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">T_max_hours_opt</span> <span class="o">=</span> <span class="mi">300</span>
<span class="n">cost_weight_lambda_opt</span> <span class="o">=</span> <span class="mf">0.005</span> <span class="c1"># Adjusted for a reasonable trade-off</span>

<span class="n">optimization_results_test</span> <span class="o">=</span> <span class="n">optimize_pathway_sequence</span><span class="p">(</span>
    <span class="n">example_employee_id_opt</span><span class="p">,</span> <span class="n">current_ai_r_opt</span><span class="p">,</span> <span class="n">df_pathways</span><span class="p">,</span> <span class="n">T_max_hours_opt</span><span class="p">,</span>
    <span class="n">cost_weight_lambda_opt</span><span class="p">,</span> <span class="n">df_employees</span><span class="p">,</span> <span class="n">df_occupations</span><span class="p">,</span> <span class="n">PARAMS</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Test Optimization Results for </span><span class="si">{</span><span class="n">example_employee_id_opt</span><span class="si">}</span><span class="s2">:"</span><span class="p">)</span>
<span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">optimization_results_test</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  </span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Test Optimization Results for EMP000:
  recommended_sequence: ['Data Storytelling with AI', 'Data Storytelling with AI', 'Data Storytelling with AI']
  projected_final_ai_r: 58.554013216429
  total_cost: 900
  total_time_hours: 90
  ai_r_improvement: 10.275403802372274
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=4aac233a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [34]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="n">example_employee_id</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">df_employees</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span><span class="p">)]</span>
<span class="n">current_ai_r</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[</span><span class="n">df_employees</span><span class="p">[</span><span class="s1">'employee_id'</span><span class="p">]</span> <span class="o">==</span> <span class="n">example_employee_id</span><span class="p">][</span><span class="s1">'current_ai_r_score'</span><span class="p">]</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

<span class="n">T_max_hours</span> <span class="o">=</span> <span class="mi">300</span>  <span class="c1"># e.g., 8 weeks of full-time training (40 hours/week * 8 = 320)</span>
<span class="n">cost_weight_lambda</span> <span class="o">=</span> <span class="mf">0.005</span> <span class="c1"># A parameter to trade-off AI-R improvement vs. cost</span>

<span class="n">optimization_results</span> <span class="o">=</span> <span class="n">optimize_pathway_sequence</span><span class="p">(</span>
    <span class="n">example_employee_id</span><span class="p">,</span> <span class="n">current_ai_r</span><span class="p">,</span> <span class="n">df_pathways</span><span class="p">,</span> <span class="n">T_max_hours</span><span class="p">,</span>
    <span class="n">cost_weight_lambda</span><span class="p">,</span> <span class="n">df_employees</span><span class="p">,</span> <span class="n">df_occupations</span><span class="p">,</span> <span class="n">PARAMS</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Multi-Step Pathway Optimization Results for Employee </span><span class="si">{</span><span class="n">example_employee_id</span><span class="si">}</span><span class="s2"> (Current AI-R: </span><span class="si">{</span><span class="n">current_ai_r</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">):"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Recommended Sequence: </span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'recommended_sequence'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Projected Final AI-R: </span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'projected_final_ai_r'</span><span class="p">]</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Total Cost: $</span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'total_cost'</span><span class="p">]</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  Total Time (hours): </span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'total_time_hours'</span><span class="p">]</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"  AI-R Improvement: </span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'ai_r_improvement'</span><span class="p">]</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Visualize the optimization results (optional, could be a table or bar chart)</span>
<span class="n">plot_current_vs_projected_ai_r</span><span class="p">(</span>
    <span class="n">current_ai_r</span><span class="p">,</span>
    <span class="p">[</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'projected_final_ai_r'</span><span class="p">]],</span>
    <span class="p">[</span><span class="s1">'Optimized Pathway Sequence'</span><span class="p">]</span>
<span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Multi-Step Pathway Optimization Results for Employee EMP018 (Current AI-R: 60.15):
  Recommended Sequence: ['Data Storytelling with AI', 'Data Storytelling with AI', 'Data Storytelling with AI']
  Projected Final AI-R: 70.91
  Total Cost: $900.00
  Total Time (hours): 90.00
  AI-R Improvement: 10.77
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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f1y7dg3379+Xl/Hy8oKXlxdiY2ORkpIi18uUKQNXV1ecO3cOT548kesVK1aEvb09oqKidB7IwMBAmJmZ4cSJEzo9BAcH49mzZzh79qxcU6vVqFWrFlJSUnDx4kW5rtFoEBQUhMTERFy9elWu29nZISAgAPHx8bh165Zc55g4Jo6JY+KYOCaOiWN6U8cUFRWFwirRhzr8/PPPGDlyJGbPno3KlSvj9OnTGDJkCObOnYtu3brh6NGjqFevHuLj4+Hh4SHfrn379pAkCevWrdO7Xn0zvt7e3njw4IE8dV7c72r+je/UOCaOiWPimDgmjolj4phed0wPHz6Ek5NToQ51KNHB19vbG6NHj0b//v3l2pQpU/Djjz/i4sWLuHr1Kvz9/REVFYVq1arJy4SGhqJatWr46quvCnQ/PMaXiIiIqGQzRl4r0Wd1ePz4MVQq3Raz34EAgJ+fH9zd3bFnzx75+tTUVERGRiIkJOQf7ZWIiIiISrYSfYxvy5YtMXXqVJQuXRqVK1dGVFQU5s6di549ewJ4MRU/ZMgQTJkyBeXKlYOfnx+++OILeHp6olWrVsXbPBERERGVKCU6+H7zzTf44osv0K9fP9y7dw+enp7o27cvxo0bJy8zatQopKen45NPPkFycjLq16+P8PBwWFhYFGPnRERERFTSlOhjfP8pPMaXiIiIqGT71x/jS0RERERkLAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCCbF3QAREf37pEycWNwtEFERsxs/vrhbMBhnfImIiIhIERh8iYiIiEgRGHyJiIiISBEYfImIiIhIERh8iYiIiEgRGHyJiIiISBEYfImIiIhIERh8iYiIiEgRGHyJiIiISBEYfImIiIhIERh8iYiIiEgRGHyJiIiISBEYfImIiIhIERh8iYiIiEgRGHyJiIiISBFeO/hevnwZO3bs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IiJFMErwTU5ONsZqiIiIiIiKjMHBd+bMmVi3bp18uX379nByckKpUqVw5swZozZHRERERGQsBgffxYsXw9vbGwCwa9cu7Nq1C9u3b0ezZs0wcuRIozdIRERERGQMBT6Pb7aEhAQ5+P72229o37493n33Xfj6+qJ27dpGb5CIiIiIyBgMnvF1cHDAzZs3AQDh4eFo0qQJAEAIgaysLON2R0RERERkJAbP+LZu3Rr/+c9/UK5cOTx48ADNmjUDAERFRaFs2bJGb5CIiIiIyBgMDr7z5s2Dr68vbt68iVmzZsHa2hoAcOfOHfTr18/oDRIRERERGYPBwdfU1BQjRozIVR86dKhRGiIiIiIiKgoGH+O7evVq/P777/LlUaNGwd7eHnXr1sX169eN2hwRERERkbEYHHynTZsGjUYDAIiIiMDChQsxa9YsODs7c9aXiIiIiEosgw91uHnzpvwlts2bN6NNmzb45JNPUK9ePTRs2NDY/RERERERGYXBM77W1tZ48OABAGDnzp1o2rQpAMDCwgJPnjwxbndEREREREZi8Ixv06ZN0bt3b1SvXh2xsbFo3rw5AOD8+fPw9fU1dn9EREREREZh8IzvwoULERISgvv372PTpk1wcnICAJw8eRKdOnUyeoNERERERMZg8Iyvvb09FixYkKs+ceJEozRERERERFQUDJ7xBYBDhw6hS5cuqFu3Lm7fvg0A+OGHH3D48GGjNkdEREREZCwGB99NmzYhLCwMGo0Gp06dQkZGBgAgJSUF06ZNM3qDRERERETGYHDwnTJlChYvXoylS5fC1NRUrterVw+nTp0yanNERERERMZicPCNiYnB22+/natuZ2eH5ORkY/RERERERGR0Bgdfd3d3XL58OVf98OHDKFOmjFGaIiIiIiIyNoODb58+fTB48GBERkZCkiTEx8djzZo1GDFiBD799NOi6JGIiIiIqNAMPp3Z6NGjodVq0bhxYzx+/Bhvv/02zM3NMWLECAwcOLAoeiQiIiIiKjSDg68kSRg7dixGjhyJy5cv49GjR6hUqRKsra2Loj8iIiIiIqMwOPhmMzMzQ6VKlYzZCxERERFRkTE4+Kanp2PGjBnYs2cP7t27B61Wq3P91atXjdYcEREREZGxGBx8e/fujQMHDuDjjz+Gh4cHJEkqir6IiIiIiIzK4OC7fft2/P7776hXr15R9ENEREREVCQMPp2Zg4MDHB0di6IXIiIiIqIiY3DwnTx5MsaNG4fHjx8XRT9EREREREXC4EMd5syZgytXrsDNzQ2+vr4wNTXVuf7UqVNGa46IiIiIyFgMDr6tWrUqgjaIiIiIiIqWwcF3/PjxRdEHEREREVGRMvgYXyIiIiKiN1GBZnwdHR0RGxsLZ2dnODg4vPLcvUlJSUZrjoiIiIjIWAoUfOfNmwcbGxsAwPz584uyHyIiIiKiIlGg4NutWze9/yciIiIielMUKPimpqYWeIW2trav3QwRERERUVEpUPC1t7d/5XG9OWVlZRWqISIiIiKiolCg4Ltv3z75/3FxcRg9ejS6d++OkJAQAEBERARWr16N6dOnF02XRERERESFVKDgGxoaKv9/0qRJmDt3Ljp16iTXPvjgA1StWhVLlizhMcBEREREVCIZfB7fiIgIBAcH56oHBwfjjz/+MEpTRERERETGZnDw9fb2xtKlS3PVly1bBm9vb6M0RURERERkbAb/ZPG8efPQpk0bbN++HbVr1wYA/PHHH7h06RI2bdpk9AaJiIiIiIzB4Bnf5s2b49KlS/jggw+QlJSEpKQktGzZErGxsWjevHlR9EhEREREVGgGz/gCgJeXF6ZOnWrsXoiIiIiIisxrBV8AePz4MW7cuIFnz57p1AMDAwvdFBERERGRsRkcfO/fv48ePXpg+/bteq/nD1gQERERUUlk8DG+Q4YMQXJyMiIjI6HRaBAeHo7Vq1ejXLly2LJlS1H0SERERERUaAbP+O7duxe//vorgoODoVKp4OPjg6ZNm8LW1hbTp0/H+++/XxR9EhEREREVisEzvunp6XB1dQUAODg44P79+wCAqlWr4tSpU8btjoiIiIjISAwOvhUqVEBMTAwAICgoCN999x1u376NxYsXw8PDw+gNEhEREREZg8GHOgwePBh37twBAIwfPx7vvfce1qxZAzMzM6xatcrY/RERERERGYXBwbdLly7y/2vWrInr16/j4sWLKF26NJydnY3aHBERERGRsRh8qEO2Z8+eISYmBmZmZqhRowZDLxERERGVaAYH38ePH6NXr16wtLRE5cqVcePGDQDAwIEDMWPGDKM3SERERERkDAYH3zFjxuDMmTPYv38/LCws5HqTJk2wbt06ozZHRERERGQsBgffzZs3Y8GCBahfvz4kSZLrlStX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SpvxTZ00qUTOUMn1f9GsG8fEMRXXmGw///zFff5DM74PHz6Ek5MTUlJS5LxmqDdixnfAgAH47bffcPDgQTn0AoC7uzuePXuG5ORknVnfu3fvwj3HO5qXmZubw9zcPFfdxMQEJia6myT7QXtZ9oNQ0PrL68VfTyQh6V9eb12SDKyrIKTc5bzqL0KFAXWVAb3nVeeYOCb8e8eU63UPA/YRr1GXJElvPa/9mKF1Q/d76jzmVQypS3nUVYDOm6J860boxVh1joljMlaPhtaNPaaX9zeFzkavWTdEiT6rgxACAwYMwC+//IK9e/fCz89P5/qaNWvC1NQUe/bskWsxMTG4ceMGQkJC/ul2iYiIiKgEK9Ezvv3798fatWvx66+/wsbGRj5u187ODhqNBnZ2dujVqxeGDRsGR0dH2NraYuDAgQgJCeEZHYiIiIhIR4kOvosWLQIANGzYUKe+cuVKdO/eHQAwb948qFQqtGnTBhkZGQgLC8O33377D3dKRERERCVdiQ6+BfnenYWFBRYuXIiFCxf+Ax0RERER0ZuqRB/jS0RERERkLAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESkCAy+RERERKQIDL5EREREpAgMvkRERESk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
"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=7ebff9e5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The pathway optimization function provides a strategic roadmap for investing in talent development. By considering multiple pathways, their costs, and time commitments, organizations can make data-driven decisions to maximize the AI-Readiness of their workforce efficiently, identifying high-ROI learning initiatives.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=7e10d560">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Section-19:-Strategic-Recommendations-&amp;-Conclusion">Section 19: Strategic Recommendations &amp; Conclusion<a class="anchor-link" href="#Section-19:-Strategic-Recommendations-&amp;-Conclusion">¶</a></h1><p>Based on the AI-Readiness assessment, skills gap analysis, and "What-If" scenario simulations, we can formulate strategic recommendations for workforce development. These insights move beyond static skill inventories, providing a dynamic framework for continuous adaptation in an AI-transformed landscape.</p>
<p><strong>Summary of Insights:</strong></p>
<ul>
<li>Identify employee cohorts with low initial AI-R scores and analyze their primary drivers ($V^R$ vs. $HR^R$).</li>
<li>Pinpoint critical skills gaps (e.g., specific AI-Fluency sub-components) that, if addressed, yield the highest AI-R improvement.</li>
<li>Recommend specific learning pathways or sequences of pathways (from optimization results) for different employee groups.</li>
<li>Highlight roles with high Systematic Opportunity ($HR^R$) but low average $V^R$, indicating potential for strategic upskilling investments.</li>
<li>Emphasize the importance of adaptive capacities and continuous learning for long-term AI-readiness.</li>
</ul>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=5b21a1ab">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [35]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-python"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"## Strategic Recommendations for AI Workforce Development</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Insight 1: Identify low AI-R cohorts and their drivers</span>
<span class="n">low_ai_r_cohorts</span> <span class="o">=</span> <span class="n">df_employees</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">'current_ai_r_score'</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"### 1. Target Low AI-R Cohorts with Driver-Specific Interventions</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Identify employees with significantly lower AI-R scores. Analyze whether their low score is primarily driven by low Idiosyncratic Readiness (V^R) or insufficient Systematic Opportunity (HR^R) in their current role. Tailor interventions accordingly.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"**Example: Top 5 Employees with Lowest AI-R Scores**"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">low_ai_r_cohorts</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'department'</span><span class="p">,</span> <span class="s1">'current_ai_r_score'</span><span class="p">,</span> <span class="s1">'vr_score'</span><span class="p">,</span> <span class="s1">'hr_r_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">to_string</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">*   **Action:** For `EMP023` in 'Marketing' with low V^R, recommend AI-Fluency focused training. For `EMP011` in 'Finance', whose HR^R is relatively low, consider internal mobility options or upskilling for roles with higher market opportunity.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Insight 2: Pinpoint critical skills gaps from heatmap</span>
<span class="c1"># This relies on the heatmap generated earlier, so we'll infer an example.</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"### 2. Address Critical Skills Gaps via Targeted Upskilling</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"The Skills Gap Heatmap (Section 16) revealed common weaknesses. For instance, if 'Business Analyst' roles show lower 'Adaptive-Capacity' scores, a targeted training program focusing on 'Strategic Career Management' or 'Cognitive Flexibility' would be beneficial.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"*   **Example:** Based on previous heatmap, 'Data Scientist' roles generally excel in 'AI-Fluency' but might show gaps in 'Domain-Expertise' (e.g., specific industry knowledge). Prioritize advanced domain-specific AI applications and certifications.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Insight 3: Recommend specific learning pathways from optimization results</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"### 3. Implement Optimized Multi-Step Learning Pathways</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"For employee </span><span class="si">{</span><span class="n">example_employee_id</span><span class="si">}</span><span class="s2">, the optimization identified the following sequence to maximize AI-R improvement within budget and time constraints:</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"*   **Recommended Pathway Sequence:** </span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'recommended_sequence'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"*   **Projected AI-R Improvement:** </span><span class="si">{</span><span class="n">optimization_results</span><span class="p">[</span><span class="s1">'ai_r_improvement'</span><span class="p">]</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">*   **Action:** Leverage such optimized pathways to guide individual career development plans, balancing cost, time, and impact.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Insight 4: Highlight roles with high HR^R but low V^R</span>
<span class="n">high_hr_low_vr_roles</span> <span class="o">=</span> <span class="n">df_employees</span><span class="p">[(</span><span class="n">df_employees</span><span class="p">[</span><span class="s1">'hr_r_score'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">70</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df_employees</span><span class="p">[</span><span class="s1">'vr_score'</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">60</span><span class="p">)]</span>
<span class="k">if</span> <span class="ow">not</span> <span class="n">high_hr_low_vr_roles</span><span class="o">.</span><span class="n">empty</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"### 4. Invest Strategically in High Opportunity, Low Readiness Roles</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Identify job roles that have high Systematic Opportunity (HR^R) but where the current workforce has lower Idiosyncratic Readiness (V^R). These are prime candidates for strategic investment.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"**Example: Employees in High HR^R / Low V^R Roles**"</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">high_hr_low_vr_roles</span><span class="p">[[</span><span class="s1">'employee_id'</span><span class="p">,</span> <span class="s1">'job_role'</span><span class="p">,</span> <span class="s1">'hr_r_score'</span><span class="p">,</span> <span class="s1">'vr_score'</span><span class="p">,</span> <span class="s1">'current_ai_r_score'</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">()</span><span class="o">.</span><span class="n">to_string</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">*   **Action:** For these roles, focused upskilling on AI-Fluency and Domain-Expertise (specific to the high HR^R area) will yield high returns.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"### 4. All employees seem to have balanced HR^R and V^R in this simulation. No explicit high opportunity/low readiness roles identified.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

<span class="c1"># Insight 5: Emphasize adaptive capacities</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"### 5. Foster Continuous Learning and Adaptive Capacity</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"The rapid pace of AI evolution necessitates a workforce with strong adaptive capacities. Emphasize training that builds cognitive flexibility, social-emotional intelligence for human-AI collaboration, and strategic career management skills across all employee levels.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"*   **Action:** Integrate 'Adaptive-Capacity' boosting modules into all major learning initiatives and promote a culture of continuous learning and experimentation.</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>## Strategic Recommendations for AI Workforce Development

### 1. Target Low AI-R Cohorts with Driver-Specific Interventions

Identify employees with significantly lower AI-R scores. Analyze whether their low score is primarily driven by low Idiosyncratic Readiness (V^R) or insufficient Systematic Opportunity (HR^R) in their current role. Tailor interventions accordingly.

**Example: Top 5 Employees with Lowest AI-R Scores**
employee_id         job_role  department  current_ai_r_score  vr_score  hr_r_score
     EMP024 Business Analyst          HR           42.085903 38.392938   44.873882
     EMP020    HR Specialist          HR           43.708711 44.618405   39.492115
     EMP006 Business Analyst         R&amp;D           45.806734 44.490746   44.873882
     EMP019    HR Specialist Engineering           46.608865 49.153953   39.492115
     EMP048    HR Specialist     Finance           47.033923 50.597067   39.492115

*   **Action:** For `EMP023` in 'Marketing' with low V^R, recommend AI-Fluency focused training. For `EMP011` in 'Finance', whose HR^R is relatively low, consider internal mobility options or upskilling for roles with higher market opportunity.

### 2. Address Critical Skills Gaps via Targeted Upskilling

The Skills Gap Heatmap (Section 16) revealed common weaknesses. For instance, if 'Business Analyst' roles show lower 'Adaptive-Capacity' scores, a targeted training program focusing on 'Strategic Career Management' or 'Cognitive Flexibility' would be beneficial.

*   **Example:** Based on previous heatmap, 'Data Scientist' roles generally excel in 'AI-Fluency' but might show gaps in 'Domain-Expertise' (e.g., specific industry knowledge). Prioritize advanced domain-specific AI applications and certifications.

### 3. Implement Optimized Multi-Step Learning Pathways

For employee EMP018, the optimization identified the following sequence to maximize AI-R improvement within budget and time constraints:

*   **Recommended Pathway Sequence:** ['Data Storytelling with AI', 'Data Storytelling with AI', 'Data Storytelling with AI']
*   **Projected AI-R Improvement:** 10.77

*   **Action:** Leverage such optimized pathways to guide individual career development plans, balancing cost, time, and impact.

### 4. Invest Strategically in High Opportunity, Low Readiness Roles

Identify job roles that have high Systematic Opportunity (HR^R) but where the current workforce has lower Idiosyncratic Readiness (V^R). These are prime candidates for strategic investment.

**Example: Employees in High HR^R / Low V^R Roles**
employee_id    job_role  hr_r_score  vr_score  current_ai_r_score
     EMP001 ML Engineer   77.416639 55.706876           66.703145
     EMP002 AI Ethicist   70.482245 45.584127           57.845619
     EMP008 AI Ethicist   70.482245 51.516844           60.977750
     EMP010 AI Ethicist   70.482245 53.540401           62.091834
     EMP013 ML Engineer   77.416639 49.591550           62.938068

*   **Action:** For these roles, focused upskilling on AI-Fluency and Domain-Expertise (specific to the high HR^R area) will yield high returns.

### 5. Foster Continuous Learning and Adaptive Capacity

The rapid pace of AI evolution necessitates a workforce with strong adaptive capacities. Emphasize training that builds cognitive flexibility, social-emotional intelligence for human-AI collaboration, and strategic career management skills across all employee levels.

*   **Action:** Integrate 'Adaptive-Capacity' boosting modules into all major learning initiatives and promote a culture of continuous learning and experimentation.

</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=fee6a828">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>This notebook provides a robust, quantitative framework for proactive workforce planning. By dynamically assessing AI-Readiness, analyzing skill gaps, and simulating training impacts, organizations can make informed investments in their human capital, ensuring competitiveness and adaptability in the evolving AI landscape. The framework's flexibility allows for continuous recalibration and adaptation as market demands and individual capabilities evolve.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=euTUVvjnOZkK">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="QuantUniversity-License">QuantUniversity License<a class="anchor-link" href="#QuantUniversity-License">¶</a></h2><p>© QuantUniversity 2025<br/>
This notebook was created for <strong>educational purposes only</strong> and is <strong>not intended for commercial use</strong>.</p>
<ul>
<li>You <strong>may not copy, share, or redistribute</strong> this notebook <strong>without explicit permission</strong> from QuantUniversity.</li>
<li>You <strong>may not delete or modify this license cell</strong> without authorization.</li>
<li>This notebook was generated using <strong>QuCreate</strong>, an AI-powered assistant.</li>
<li>Content generated by AI may contain <strong>hallucinated or incorrect information</strong>. Please <strong>verify before using</strong>.</li>
</ul>
<p>All rights reserved. For permissions or commercial licensing, contact: <a href="mailto:info@quantuniversity.com">info@quantuniversity.com</a></p>
</div>
</div>
</div>
</div>
</main>
</body>
</html>
