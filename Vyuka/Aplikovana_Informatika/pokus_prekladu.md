Apríl 2023 (verzia 1.78)

Zobraziť poznámky o vydaní po aktualizácii

Vitajte vo vydaní Visual Studio Code v apríli 2023.V tejto verzii je veľa aktualizácií, ktoré dúfame, že sa vám bude páčiť, niektoré z kľúčových zvýraznení zahŕňajú:

Vylepšenia prístupnosti - lepšia podpora čítačky obrazovky, nové zvukové narážky.
Nové farebné témy - „Moderné“ svetlo a tmavá farba predvolené.
Šablóny profilu - vstavané šablóny pre Python, Java, Data Science a ďalšie.
Drag and Drop Selector - Vyberte, ako by ste chceli odkazy na položky umiestnené do editora.
Samostatný farebný zberač - UI farebného zberu na vloženie alebo úpravu farebných formátov.
Rýchle opravy pre vstup riadenia zdroja - Opravte pravopis a ďalšie chyby priamo vo vstupnom políčku.
Markdown Drag and Drop Videá - ľahko pridajte značky videa do súborov Markdown.
Notebooky Vložte obrázky ako prílohy - vyberte medzi odkazom, cestu alebo prílohu.
GIT LFS a VS kód pre web - Použite VSCode.dev pre repos s veľkým úložiskom GIT veľkého súboru.
VS Code Day 2023 - dohnať relácie v zozname skladieb YouTube.
Ak si chcete prečítať tieto poznámky k vydaniu online, prejdite na aktualizácie na adrese code.visualStudio.com.

Zasvätení: Chcete čo najskôr vyskúšať nové funkcie?Hneď ako budú k dispozícii, môžete si stiahnuť nových zasvätených osôb a vyskúšať najnovšie aktualizácie.

Dostupnosť
Nastavenia ARIA Verbosity
Používatelia snímačov obrazovky môžu vylúčiť rady z funkcie Aria-label, aby sa znížila redundancia prostredníctvom nastavení „prístupnosť.verbozity.diff-editor“ a „prístupnosť.Verbosity.terminal“.

Vylepšené a zarovnané skúsenosti s rýchlym výberom
Predtým používatelia režimu prístupnosti zažili pri práci s paletou príkazu a ďalšími rýchlymi výbermi odlišné správanie.V režime prístupnosti nebola vybraná prvá položka rýchleho výberu, aby bola úplne prístupná.Táto iterácia, zaviedli sme nové správanie, ktoré vám umožní mať to najlepšie z oboch svetov: prístupný a rýchly rýchly pracovný postup, ktorý vám umožňuje okamžite zasiahnuť Enter.

Poznámka: Jedným z kompromisov s týmto prístupom je, že ak je vybratá položka pri rýchlom výbere, nemôžete počuť zmeny ARIA v vstupnom políčku Quick Pick, kvôli obmedzeniu ARIA.Ak chcete počuť tieto zmeny, môžete stlačiť Shift Neznáme kartu, kým nie je vybratá žiadna položka zoznamu.

Terminal
Terminal accessible buffer improvements
Jump between commands using Ctrl+DownArrow and Ctrl+UpArrow.
Use Set Selection Anchor, Select from Anchor to Cursor, and page navigation via Shift+PageUp and Shift+PageDown.
Preview the position when using Terminal: Navigate Accessible Buffer (Ctrl+Shift+O) before accepting a command to go to a new location.
Engage with the output while dynamic updates occur.
Terminal Accessibility Help menu
The terminal's Accessibility Help menu can now be navigated using arrow keys.

Diff editor audio cue improvements
VS Code now caches audio cues so they only have to be loaded once, yielding better responsiveness, and have improved the tones used for the diff editor.

Go to Line/Column announcement
When Go to Line/Column... (Ctrl+G) is invoked, the screen reader now reads the associated line content.

Workbench
New default Color Themes
New 'Dark Modern' and 'Light Modern' themes replace 'Dark+' and 'Light+' as the new default dark and light color themes.

Dark Modern and Light Modern color themes

Profile templates
Profiles let you quickly switch your editor extensions, settings, and UI layout depending on your current project or task. To help you get started with profiles, we are shipping Profile Templates, which are curated profiles for different programming languages and scenarios. You can use a profile template as is or use it as a starting point to customize further for you own workflows.

You select a profile template through the Profiles > Create Profile... dropdown:

Create Profile dropdown with profile templates

Once you select a profile template, you can review the settings, extensions, and other data, and remove individual items if you don't want to include them in your new Profile.

Profiles view showing the contents of the Data Science profile template

After you create the new profile based on a template, changes made to settings, extensions, or UI are persisted to your profile.

Glyph margin decoration rendering improvements
This month, we've improved the rendering of decorations that appear in the editor margin. Debugging-related decorations such as breakpoints and stack frame pointers will always render next to the editor line numbers. Additional decorations render to the left of any debugging-related decorations. This allows you to view your breakpoints even if there are other decorations on the same line, such as test decorations or bookmarks. Note that clicks are not yet scoped to individual decorations.

bookmarks displayed next to breakpoint and stack frame pointer decorations

Copy images from the image preview
You can now copy images from the built-in image preview using Ctrl+C or by right-clicking in the preview and selecting Copy. The copied image data can be pasted back into VS Code or into other applications.

Editor
Drop selector
VS Code lets you drop files and content into text editors by holding Shift before dropping. In this update, we've added UI that lets you change how this content is inserted into the file. After you drop an image into a Markdown file for example, this control lets you switch between inserting a Markdown image, a workspace relative path to the image, and the full path to the image:


The drop selector control appears whenever you drop content and there is more than one possible way it could be inserted. You can open the control by clicking on it or using Ctrl+.. The drop selector goes away as soon as you start typing or move the cursor outside of the inserted text. You can also fully disable the drop selector control using "editor.dropIntoEditor.showDropSelector": "never".

VS Code includes a few built-in ways to drop common content formats. Extensions can also add their own drop options using the DocumentDropEditProvider API.

Standalone color picker
It is now possible to launch a standalone color picker in order to insert and replace colors. To open the color picker, select Show or Focus Standalone Color Picker from the Command Palette.

Standalone color picker control adjusted to blue color

When no colors or color formats are provided by extensions, the color-picker falls back to CSS-formatted colors. It is also now possible to visualize inline color decorators for CSS-formatted colors in all file types. To display these decorators, enable the Editor: Default Color Decorators (editor.defaultColorDecorators) setting.

New snippet variable for timezone offset
A new snippet variable, CURRENT_TIMEZONE_OFFSET, is now available. This variable returns the current timezone offset in the format +HHMM or -HHMM (for example -0700). This complements other time-related snippet variables such as CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY_NAME, etc.

Diff algorithm improvements
We continued improving the new diff algorithm in VS Code and deprecated the old algorithm. While the old algorithm is still the default for the diff editor, we will slowly change the default to the new algorithm and measure its performance.

You can override the default by setting diffEditor.diffAlgorithm to advanced (new diff algorithm) or legacy (default).

The new algorithm produces better diffs in many cases, but might be slower for some documents.

Here are some examples (legacy vs. advanced):

Improved line insertion diffs by considering indentation:

JSON file diff result using legacy algorithm

JSON file diff result using advanced algorithm

Improved word insertion diffs by considering space and separator characters:

TypeScript imports word insertion diff using legacy algorithm

TypeScript imports word insertion diff using advanced algorithm

More natural diffs by minimizing not just the length of the diff, but also the number of chunks:

TypeScript added line diff using legacy algorithm

TypeScript added line diff using advanced algorithm

Less noise by extending character level diffs to entire words if a part of the word changed significantly:

TypeScript code change diff using legacy algorithm

TypeScript code change diff using legacy algorithm

Diffing source code and even just evaluating the quality of a diff are hard problems and there is still room for improvement. If you encounter a diff where you think the algorithm could do better, try out our diff playground and share your feedback and ideas in our issue tracker!

Inline completion improvements
This iteration we rewrote the inline completion feature and fixed a lot of bugs.

Most notably, Accept Word now works across lines and there is a new command Accept Line. To support this feature, accepting the next word/line does not ask the extension again, as inline completion provider extensions would often report entirely different suggestions when asking for inline completions of the next line.

Extensions
Improved extension recommendations notification
The extension recommendations notification now shows the publisher of the recommended extension. This helps you make a more informed decision before installing the extension. The following images show the new notification when there are recommendations for both a single extension and multiple extensions.

Extension recommendations notification with a single recommendation Extension recommendations notification with multiple recommendations

Informing about installed deprecated extensions
If you have an extension installed that has been deprecated, you will now receive a notification informing you about it and suggesting alternatives. This is shown only once per deprecated extension.

Notification about deprecated extension

Source Control
Quick Fixes in the Source Control input
Code Actions and Quick Fixes are now supported in the Source Control message box:


The Code Spell Checker extension, for example, adds spelling fixes to the Source Control input. Extensions can contribute additional fixes and Code Actions.

GitHub repository rulesets
VS Code already lets you define branch protection using the git.branchProtection setting. This milestone we added a new experimental feature that uses the recently announced GitHub repository rulesets to determine whether a branch is protected. If you are using GitHub repository rulesets, you can enable this feature using the github.branchProtection setting.

Notebooks
Drop image files into notebooks to create attachments
You can now drag and drop image files into notebook Markdown cells to create attachments. When you drop the image, use the new drop selector control to select Insert Image as Attachment:

Using the drop selector in a notebook Markdown cell

This adds the image to the notebook as an attachment instead of simply adding a link to the image:

An image file added as an attachment

Toggle notebook output scrolling
You can now toggle individual cells to display output in a scrollable region either by command Notebook: Toggle Scroll Cell Output (Ctrl+K Y) or the link in the truncation message.


Find control improvements
The notebook Find control now searches keywords on what's visually presented by default. Users can change the search scope (Markdown source, Markdown preview, code source, and code outputs) through setting notebook.find.scope. Additionally, when replacing matches, the Markdown cell is converted to an editable cell so you can make the replacement. When you're done, the cell is converted back to Markdown, and the preview is restored.


Languages
Drag and drop videos into Markdown files
Want to insert a video into your Markdown? Just drag it into the editor and then hold Shift to drop it into the file:


This inserts a <video> tag pointing to the video file. You can drag videos from VS Code's Explorer or from your local operating system.

Strict nulls for JavaScript script blocks in HTML
You can now use the js/ts.implicitProjectConfig.strictNullChecks setting to enable strict nulls for JavaScript in HTML script blocks:

Strict nulls in a script block

With strict nulls enabled, hovers and other IntelliSense features show when a type can be nullable. For example, notice how el now has a type of HTMLElement | null. This is because document.getElementById returns null if it can't find an element with that ID.

Testing
Continuous run can now be turned on for individual tests. This requires a test extension that supports continuous run and has adopted the supportsContinuousRun API finalized last iteration.

Continuous run button highlighted on an individual test

VS Code for the Web
Commit files to Git Large File Storage
Git Large File Storage (LFS) allows you to efficiently store large files in Git repositories. github.dev and vscode.dev now support committing files to Git LFS in repositories hosted on GitHub, enabling easy updates from your browser without needing to install the LFS extension for Git locally.

LFS commit support in github.dev and vscode.dev works out of the box when your repository already has a .gitattributes file in the root of your repository that specifies which file types should be stored with Git LFS. To set up your repository for Git LFS for the first time, consult the Git LFS documentation.

Remote Development
The Remote Development extensions, allow you to use a Dev Container, remote machine via SSH or Remote Tunnels, or the Windows Subsystem for Linux (WSL) as a full-featured development environment.

You can learn about new extension features and bug fixes in the Remote Development release notes.

And check out the Develop Anywhere with VS Code VS Code Day session.

Contributions to extensions
Python
Jupyter extension no longer installed by default
The Jupyter extension is no longer automatically installed alongside the Python extension by default. This change was made in response to feedback from Dev Container users who wanted a faster container creation process without the Jupyter extension installed by default.

If you have Dev Container definitions that only list the Python extension and wish to continue using the Jupyter notebooks features in your containers, you can add the Jupyter extension ID to your devcontainer.json file:

  "customizations": {
    "vscode": {
      "extensions": ["ms-python.vscode-pylance", "ms-python.python", "ms-toolsai.jupyter"]
    }
  }

Alternatively, you can create a Profile that includes the Python and Jupyter extensions, as well as any other of your favorite extensions.

Create environment command with microvenv
When the Python: Create environment command is invoked using a Python distribution that doesn't have the venv package installed, the Python extension now uses microvenv as a fallback. This can be a hurdle for Python environments that are preinstalled on Unix-based systems.

Microvenv is a lightweight Python module that offers a minimalist approach to creating virtual environments for your Python projects. It is not equipped with traditional activation scripts like virtual environments, but it provides a good alternative for creating an isolated environment when the venv module is not available in your Python distribution.

The Create Environment command will also install pip into the environments created via microvenv.

Formatter extension recommendations
In previous releases, we announced new extensions for the Black Formatter and autopep8 that work in tandem with the Python extension through the Language Server Protocol (LSP) to provide formatting for Python files. In this release, we display a notification if you are still using the Python extension's built-in formatting features, prompting you to install these new extensions.

Run Python actions are now in submenus
In order to streamline the Python commands available when right-clicking on the editor, the Run Python File in Terminal and Run Selection/Line in Python Terminal commands are now submenu items under the Run Python entry.

Run Python option on context menu with "Run file in terminal" and "Run selection/line" options in the submenu

Automatic conversion of f-strings
There's a new "python.analysis.autoFormatStrings" setting that enables automatic conversion of f-strings when using Pylance. Once enabled, Pylance will automatically insert an f at the beginning of a string when you insert { within quotes:


The default value for this setting is currently disabled, but will be enabled in an upcoming release pending positive feedback. If you have any comments or suggestions regarding this feature, feel free to share them on the Pylance GitHub repository.

Code navigation enabled on strings that contain paths
There's another new experimental setting called "python.analysis.gotoDefinitionInStringLiteral" that enables Go to Definition from module-like string literals. This can be helpful if you're working on web applications, such as Django apps, and want to navigate to modules or paths defined in string literals:


This new setting, like the autoFormatStrings setting mentioned earlier, is currently disabled by default. However, we plan to enable this behavior in a future release based on feedback. Eventually, we plan to remove this setting entirely.

Jupyter
Restart commands
The Jupyter extension now includes two new commands, enabling the user to restart the kernel and run cells directly. The commands are Restart Kernel and Run All Cells and Restart Kernel and Run Up To Selected Cell, and can be accessed via the command IDs jupyter.restartkernelandrunallcells and jupyter.restartkernelandrunuptoselectedcell respectively.

Reconnect to busy remote Jupyter kernels
In previous releases, when connecting to a remote Jupyter kernel session, the Jupyter extension would wait for the kernel to be idle before connecting. This could take a long time if the kernel was busy running a long-running computation. In this release, the Jupyter extension connects to the kernel immediately, even if it is busy. This allows you to interrupt the kernel while it is busy.

Platform-specific Jupyter extensions
The Jupyter extension now ships platform-specific extensions, with each VSIX built for a specific platform (Windows 64 bit, Windows 32 bit, Linux x64, Alpine x64, macOS Intel, macOS Apple Silicon, etc.). The download size of the Jupyter extension for individual platforms is smaller, resulting in faster download times and less disk space usage.

GitHub Pull Requests and Issues
There has been more progress on the GitHub Pull Requests and Issues extension, which allows you to work on, create, and manage pull requests and issues. Highlights include:

You can add team reviewers to a pull request.
All of the places where you can Checkout default branch now respect the git.pullBeforeCheckout setting.
GitHub's file level commenting is supported.
Review the changelog for the 0.64.0 release of the extension to learn about the other highlights.

GitHub Copilot
Note: To get access to the new chat-based GitHub Copilot features, you'll need to sign up for the GitHub Copilot chat waitlist. These features are only available in VS Code Insiders with the GitHub Copilot Nightly extension.

Chat editors
Our first iteration on GitHub Copilot Chat enabled chat sessions in the sidebar. Now, we support opening the same chat view as an editor. This lets you customize the position of your chat session to be anywhere you want within your window layout.

You can open a chat editor by running the command Interactive Session: Open Editor and then move it between editor groups just as you would with any other editor.

A chat view as an editor

Additional codeblock commands
There are two new commands in the codeblock toolbar, Insert into New File and Run in Terminal. These are next to the existing commands Copy and Insert at Cursor, and give you extra options for quickly taking action on the code suggestions that are returned from Copilot.

The codeblock toolbar showing the two new codeblock commands

Code Actions and inline chat
Editor chat sessions are now integrated with the Quick Fixes. Select the light bulb for a squiggle and there are options to fix or explain using Copilot.


In addition to Code Actions, inline chat is now also available from the editor context menu.

Inline chat modes
There is now a setting to change the different modes of inline chat: interactiveEditor.editMode.

The options are:

live - Apply AI suggested changes directly to the editor (default).
livePreview - Apply changes but renders them in an embedded diff editor.
preview - Show changes in a disconnected, embedded diff editor.
Similar commands in the Command Palette
With the power of Copilot, the Command Palette is now able to show similar command results. To enable this, you must have an active Copilot subscription, be in the private preview of the chat view, and apply the setting:

"workbench.commandPalette.experimental.useSemanticSimilarity": true

Here are some examples:

"turn on autosave" being interpreted as Toggle Auto Save

query "turn on autosave" is correctly resolved to Toggle Auto Save

"add function" includes additional results at the bottom with contributions from extensions

query "add function" including Azure Functions Create Function command

Lastly, if your results yield no results, you can Ask GitHub Copilot, which puts what's in your filter box in a new chat for Copilot to handle.

Ask GitHub Copilot "no results" option in the Command Palette

We will be iterating in this space so stay tuned!

Preview Features
TypeScript 5.1 Support
This update includes support for the upcoming TypeScript 5.1 release. Read the TypeScript 5.1 Beta blog post and TypeScript 5.1 iteration plan for more details on what the TypeScript team is currently working on. Some editor tooling highlights:

Linked editing support for JSX tags.
Snippet completions for @param JSDoc tags.
To start using the TypeScript 5.1 nightly builds, install the TypeScript Nightly extension.

Rename matching JSX tags using F2
When you trigger rename on a JSX tag, VS Code now renames just the matching tag instead of trying to update all references to the tag:


This requires TypeScript 5.1+ and matches how rename works in HTML.

You can disable this behavior using javascript.preferences.renameMatchingJsxTags and typescript.preferences.renameMatchingJsxTags.

Extension authoring
Workspace edits can now create files directly from DataTransferFile
One of the primary uses of the drop into editor API is writing dropped files/content into the workspace. However in previous VS Code releases, this could be fairly slow for large files. This is because the file contents end up being copied between processes twice: first from the renderer to the extension host to read the file contents, and then back from the extension host to the renderer to write the file.

class CreateFileDropProvider implements vscode.DocumentDropEditProvider {
    async provideDocumentDropEdits(_document: vscode.TextDocument, _position: vscode.Position, dataTransfer: vscode.DataTransfer, _token: vscode.CancellationToken): Promise<vscode.DocumentDropEdit | undefined> {
        const pngFile = dataTransfer.get('image/png')?.asFile();
        if (!pngFile) {
            return;
        }

        // Read file
        // This results in the entire file contents being copied over to the extension host.
        const contents = await pngFile.data();

        // Now create a workspace edit that writes the file into the workspace
        // This results in the same file contents from above being copied back again.
        const additionalEdit = new vscode.WorkspaceEdit();
        const path = vscode.Uri.joinPath(vscode.workspace.workspaceFolders![0].uri, 'image.png');
        additionalEdit.createFile(path, { contents });

        const edit = new vscode.DocumentDropEdit(path.fsPath);
        edit.additionalEdit = additionalEdit;
        return edit;
    }
}

Now you can avoid those extra copies though by passing a DataTransferFile directly to WorkspaceEdit.createFile:

additionalEdit.createFile(path, { contents: pngFile });

This should significantly improve performance, especially when working with larger files.

Resolve Code Action commands in resolveCodeAction
A CodeActionProvider can now lazily resolve the command of CodeAction in resolveCodeAction. Previously only the edits for the Code Action could be lazily resolved.

If the command is expensive to compute, this allows a CodeActionProvider to defer this work until the Code Action is going to be applied.

editor/lineNumber/context menu
We have finalized the editor/lineNumber/context menu. This allows extension authors to contribute actions to a context menu anchored to the editor line number and glyph margin. Actions contributed to this menu receive the line number in command arguments and can reference the editorLineNumber context key in their when clauses.

Authentication API improvements
Authentication session preference is now workspace aware
For authentication providers that support being signed into multiple accounts at once (like Microsoft), the user is prompted to select an account to use when vscode.authentication.getSession with createIfNone: true is called.

Previous behavior:

This preference is remembered until vscode.authentication.getSession is called with the ClearSessionPreference flag.

New behavior:

This preference is remembered per-workspace until vscode.authentication.getSession is called in that workspace with the ClearSessionPreference flag.

This behavior was introduced to allow extensions to use different accounts for different workspaces and allow those preferences to be remembered.

Note: The preference is extension specific. So if one extension calls vscode.authentication.getSession, it will not affect the session preference for another extension calling vscode.authentication.getSession.

Microsoft Sovereign Cloud support in desktop
This iteration, we introduced a new Authentication Provider into the core product: Microsoft Sovereign Cloud. This provider is for authenticating users to Microsoft Cloud for Sovereignty like Azure US Government, Azure China, etc. Under the hood, it works identically to the Microsoft auth provider, only with different URLs. If you want to use this auth provider, you can guide the user through setting the microsoft-sovereign-cloud.endpoint value, which has a couple of defaults but also supports custom Sovereign Cloud URLs as well.

Keep in mind that most users do not have a Sovereign Cloud account. Our recommendation is that if you want to support Sovereign Clouds, you should make it possible for users to sign in via Sovereign Clouds, but not include it as part of the mainline workflow so as not to confuse users.

Proposed APIs
Every milestone comes with new proposed APIs and extension authors can try them out. As always, we want your feedback. Here are the steps to try out a proposed API:

Find a proposal that you want to try and add its name to package.json#enabledApiProposals.
Use the latest vscode-dts and run vscode-dts dev. It will download the corresponding d.ts files into your workspace.
You can now program against the proposal.
You cannot publish an extension that uses a proposed API. There may be breaking changes in the next release and we never want to break existing extensions.

Format multiple ranges
The DocumentRangeFormattingEditProvider API has an optional proposed function to support formatting multiple ranges at once. By adopting this API, providers improve the format modified ranges flow because only a single request to a language service is needed.

Document drop metadata
This new proposal enriches the existing drop into editor API to support the new drop selector. Providers can use it to provide a better drop into editor experience.

The first part of this proposal adds a label property to DocumentDropEdit. This human readable label describes the edit and is shown in the drop selector UI:

Labels shown in the drop selector

The second part adds an extra metadata argument to registerDocumentDropEditProvider. This metadata argument identifies the provider and tells VS Code the types of content it applies to:

vscode.languages.registerDocumentDropEditProvider('markdown', new InsertBase64ImageProvider(), {
    // Unique id that identities this provider
    id: 'insertBase64Image',

    // Array of mime types, such as `image/png` or `text/plain`, that this provider supports.
    // You can also use wildcards, such as `image/*` which matches any image content that is dropped.
    dropMimeTypes: ["image/*"]
})

The dropMimeTypes array can help improve performance as your provider is only called for relevant dropped content.

Engineering
Electron 22 update
In this milestone, we have finished our experiment with using a custom allocator for extension host and are ready to bundle Electron 22 into VS Code Desktop. We want to thank everyone involved with self-hosting on Insiders builds and provided early feedback. This update comes with Chromium 108.0.5359.215 and Node.js 16.17.1.

VS Code Day
You can catch up on all the highlights from VS Code Day with the VS Code Day 2023 YouTube playlist. There you will find sessions on topics such as GitHub Copilot, Data Science, and TypeScript, as well as the Keynote by Erich Gamma and Kai Maetzel, where they explain how the team builds and ships VS Code.

Thank you
Last but certainly not least, a big Thank You to the contributors of VS Code.

Issue tracking
Contributions to our issue tracking:

@gjsjohnmurray (John Murray)
@IllusionMH (Andrii Dieiev)
@starball5 (starball)
@tamuratak (Takashi Tamura)
@Kathund (Kath)
@ArturoDent (ArturoDent)
Pull requests
Contributions to vscode:

@a-stewart (Anthony Stewart): Support copying non-pngs and wait for focus to avoid race conditions PR #180322
@andrewbranch (Andrew Branch): [typescript-language-features] Support replacing Go to Definition with Go to Source Definition by preference PR #178840
@c-claeys (Cristopher Claeys): Add support for multiRange formatting PR #163190
@donaldnevermore (Donald33 Wang): Support custom switch-case indentation PR #179670
@FlorentRevest (Florent Revest): debug session: use queue to make sure debugee status get processed in correct order PR #180410
@gjsjohnmurray (John Murray): Set a max-height on comments and add vertical scrolling (#174629) PR #180044
@hermannloose (Hermann Loose): Allow individual comments to be marked as draft PR #173305
@iliazeus (Ilia Pozdnyakov): Add support for F20-F24 keys in keyboard shortcuts PR #179591
@jeanp413 (Jean Pierre): Fixes configured default shell not used when connecting to remote PR #175844
@jjaeggli (Jacob Jaeggli): Accessibility help dialog uses semantic markup for assistive technology PR #179726
@KapitanOczywisty: Update PHP grammar from fork PR #180100
@LakshyAAAgrawal (Lakshya A Agrawal): Fix typo in vscode.d.ts PR #177377
@mahmoudsalah1993 (Mahmoud Salah): Return the key correctly when having a single userDataProfileContentH… PR #178517
@Mai-Lapyst: Fix accidently starting all onTaskType extensions when running any task; fixes #175821 PR #178679
@maxmmyron (Max): Fix: diff editor arrow click enables breakpoint PR #179130
@mblout (Michael Blout): Add debug API for call stack selection changes (63943) PR #179132
@MonadChains (MonadChains): Issue 151220/add current timezone offset variable PR #170518
@simon04 (Simon Legner): terminalActions: "Open Last URL" PR #173217
@SimonSiefke (Simon Siefke): fix: printing of extension id in mainThreadExtensionService PR #179553
@spahnke (Sebastian Pahnke): [Monaco] Add monaco.editor.registerEditorOpener method to be able to intercept editor open operations PR #177064
@sumneko (最萌小汐): Update Lua grammar PR #177798
@tisilent (xie jialong 努力鸭): Fix #159471 PR #177961
@tomheaton (Tom Heaton): Fix collapseAll command when no folder is open PR #180330
@weartist (Han)
support to open both integrated terminal and external terminal with … PR #168879
Added support for breakpointWidget to automatically adapt to width wh… PR #179551
add confirmation before removing cell for #173481 PR #179776
@Wundero (Sam Riddle): Use defined variable instead of internal property PR #178701
@yiliang114 (易良)
fix: close #176763, modify the conditions to load vscode-web-playground PR #176771
chore: rename wrong service name PR #177954
fix: typos PR #179581
@YinDongFang (dongfang): Fix 'Window' key is treated as 'unknown' in Firefox (#175739) PR #175740
Contributions to vscode-js-debug:

@markw65: Fix the race for the javascript terminal too PR #1654
Contributions to vscode-json-languageservice:

@zardoy (Vitaly)
[completions] Always show details such as Default value PR #183
[completion] Don't suggest duplicates when uniqueItems: true PR #184
Contributions to vscode-pull-request-github:

@Balastrong (Leonardo Montini)
Add x button to remove a label from a new PR PR #4649
Change file mode for execute husky hook on MacOS PR #4695
@eastwood (Clinton Ryan): Gracefully handle errors where the SSH configuration file is corrupt or malformed PR #4644
@kabel (Kevin Abel)
Fix status checks rendering PR #4542
Make the display of PR number in tree view configurable PR #4576
Centralize all configuration strings into settingKeys.ts PR #4577
Move PullRequest to a shared location for reviewing of types PR #4578
@ypresto (Yuya Tanaka): Fix wrong repo URL for nested repos in workspace (fix copy permalink) PR #4711
Contributions to monaco-editor:

@dneto0 (David Neto): Add WebGPU Shading Language tokenizer, with tests PR #3884
@kisstkondoros (Tamas Kiss): Fix reference error in convert method of OutlineAdapter PR #3924
@tamayika: Change moduleResolution to node16 and adopt TS 5.0 PR #3860
Contributions to devcontainers/cli:

@aaronlehmann (Aaron Lehmann): Add support for Docker credential helpers PR #460
