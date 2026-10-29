# Nature Skills 中文使用指南

整理日期：2026-10-28。来源：[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)。版本固定为 `c1637a89c7097d486ba1c6e755e34d01cbb24998`。

## 安装与开始使用

本次安装包括 23 个可触发技能和 1 个 nature-shared 共享支持包，保留完整目录结构。目标目录：`~/.codex/skills/`。安装技能文件不会自动配置数据库账号、API、Python/R 依赖、OCR、Office 渲染工具或定时任务。已逐一核对全部 814 个文件与上游 Git blob 哈希，未发现缺失或内容差异。技能文件共 40,065,183 字节（约 38.2 MiB；实际磁盘分配略有差异）。安装核验结果见同目录《nature-skills安装核验.json》。

下一轮对话即可使用。若界面尚未显示，打开新聊天再试。最稳妥的调用方式是明确写“使用 nature-reader”这类名称，并附上材料、目标、输出格式和保存目录。nature-proposal-writer 的声明名称实际是 `researchwrite`，建议写“使用 researchwrite（nature-proposal-writer）”。nature-shared 无需单独调用，也不要单独删除。

这些是第三方科研工作流，名称中的 Nature 不代表 Nature 期刊官方产品或录用保证。期刊具体要求仍应在投稿时核查最新官网。

通用提示词：

> 使用【技能名】，处理【附件或路径】。目标是【具体结果】，面向【读者】，输出【格式】并保存到【目录】。只依据已提供或可核验的材料，缺失事实单列。我的电脑为 8GB 内存，请串行处理，依赖按需配置。

## 快速选技能

| 你想做什么 | 优先技能 |
|---|---|
| 查文献与引用指标 | `nature-academic-search` |
| 下载论文全文 | `nature-downloader` |
| 给论点找支撑引用 | `nature-citation` |
| 核验参考文献 | `nature-ref-verifier` |
| 持续跟踪新文献 | `nature-literature-pipeline` |
| 全文中英对照阅读 | `nature-reader` |
| 讲透论文的推理 | `nature-paper-xray` |
| 生成结构化精读卡 | `nature-paper-card` |
| 保留版式的中文 PDF | `nature-paper-trans` |
| 论文变组会 PPT | `nature-paper2ppt` |
| 截图变可编辑 PPT | `nature-image2ppt` |
| 学术稿件排版成 Word | `nature-paper2word` |
| 整理实验记录 | `nature-experiment-log` |
| 检查统计报告 | `nature-statistics` |
| 制作与审查科研图 | `nature-figure` |
| 开题与研究方案 | `researchwrite` |
| 社科选题与论证 | `nature-social-science` |
| 起草和重构论文章节 | `nature-writing` |
| 润色与学术翻译 | `nature-polishing` |
| 投稿前模拟审稿 | `nature-reviewer` |
| 回复真实审稿意见 | `nature-response` |
| 数据与代码可用性说明 | `nature-data` |
| 论文与技术资料转专利草稿 | `nature-paper-to-patent` |

## 容易混淆的区别

- **reader / paper-trans**：reader 输出可搜索、可继续利用的中英对照 Markdown；paper-trans 输出尽量保留布局的中文图片 PDF，没有 OCR 文字层，通常需要逐页生图。日常阅读优先 reader。
- **paper-xray / paper-card / reviewer**：xray 重在讲懂作者推理和公式；card 重在固定结构、来源与证据链的长期笔记；reviewer 重在投稿风险和正式评审式意见。
- **paper2ppt / image2ppt**：前者根据论文内容创作汇报，后者还原已有截图或扫描页面。
- **writing / polishing / researchwrite**：writing 起草或重建论文章节；polishing 修改已有文本；researchwrite 适合先设计研究方案和论证结构。
- **academic-search / citation / ref-verifier / literature-pipeline**：分别是搜文献、给论点补引用、核验已选文献、持续跟踪新文献。
- **writing / response**：首次投稿材料由 writing 处理，返修信与逐点回复由 response 处理。

## 每个技能怎么用

### 1. nature-academic-search：查文献与引用指标

跨数据库搜索、DOI 核查、引用格式、他引和引用者分析。

**直接这样说**

> 使用 nature-academic-search，围绕【研究主题】检索近五年论文，先列检索式，再筛选 10 篇，提供 DOI、来源和筛选理由。

**需要材料**

- 检索主题、关键词、时间范围、期刊范围或目标文献 DOI。
- 是否允许使用 Scopus / ScienceDirect 等需要本机配置的来源。
- 严格他引的排除口径，例如是否排除同机构、共同作者或课题组网络。

**得到什么**

- 去重后的文献表，包含标题、作者、年份、期刊、DOI 和来源。
- 引用格式文本或 `.ris`、`.bib`、`.nbib`、`.enw` 等文献管理文件。
- 严格他引统计表和引用上下文摘要。
- 查询策略、数据源说明和无法验证的条目列表。

**依赖与配置**

- PubMed 检索需要配置 `PUBMED_EMAIL` 或 `mcp-server/config.toml`。
- Scopus / ScienceDirect 依赖本机 `pybliometrics` 配置，默认读取 `~/.config/pybliometrics.cfg`。
- 不要把 Elsevier API key 写入仓库文件；只在本机安全配置中保存。

**使用边界**

- 二级学术索引只能作为发现线索，关键字段应回到 DOI、PubMed、出版社页面或数据库记录核实。
- 严格他引判断需要明确排除规则；没有作者/机构信息时会标注不确定。
- 无权限数据库不会被绕过，只会报告缺失来源或需要用户登录。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-academic-search/README.md)

### 2. nature-downloader：下载论文全文

通过开放获取、合法仓储、出版社 API 或学校授权获取全文。

**直接这样说**

> 使用 nature-downloader，按这份 DOI 清单下载论文，只要正文，不下载补充材料，优先开放获取；按顺序处理，已有文件跳过，保存到【目录】。

**使用边界**

- 不绕过付费墙，不使用镜像站，也不读取或导出 cookie、密码、localStorage 或 session 文件。
- 对可见滑块、复选框、机器人校验或简单确认按钮，只在同一已授权浏览器标签页中最多尝试两次，并在页面确认成功后继续。
- 图片选择、二维码确认、短信/OTP、通行密钥、硬件密钥或双重认证必须由用户本人完成。
- 没有合法访问权限时，只报告状态、失败原因和可能替代路线。

**特别说明**：提供 DOI、题名或合法全文链接，明确“只正文”或“含补充材料”。可能需要学校入口、本人登录或出版商授权，结果不保证都是 PDF；下载清单会记录格式、访问路径和失败原因。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-downloader/README.md)

### 3. nature-citation：给论点找支撑引用

将段落拆为论点，限定 Nature/Science/Cell 及子刊寻找支持证据。

**直接这样说**

> 使用 nature-citation，为下面的引言逐条匹配近五年 CNS 及子刊支撑文献，说明支撑位置与证据偏差，并导出 RIS：【段落】。

**需要材料**

- 待引用的段落、claim 列表、DOI 清单或 PMID 清单。
- 期刊范围、时间范围、是否允许综述、是否只要旗舰刊。
- 目标引用格式和导出格式，例如 `RIS`、`ENW` 或 Zotero `RDF`。

**得到什么**

- claim 分段表和候选文献表。
- 每个 claim 的建议插入位置、候选 DOI、期刊、年份和支撑说明。
- 可选的 JSON、TSV、Markdown、HTML 审查材料。
- 可导入文献管理器的引用文件。默认使用 RIS，EndNote 导入时选择 `Reference Manager (RIS)`。

**使用边界**

- 只把论文作为候选支撑，不会替作者保证其必然适合最终引用。
- 不会使用博客、新闻稿或搜索摘要作为唯一依据。
- 当文献只能支撑相邻但不完全相同的 claim 时，会明确标注证据偏差。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-citation/README.md)

### 4. nature-ref-verifier：核验参考文献

逐字段核对作者、题名、年份、期刊、卷期页码和 DOI。

**直接这样说**

> 使用 nature-ref-verifier，逐条核查这份参考文献，列出原记录、可靠来源、差异与建议改法，无法验证的单独列出。

**需要材料**

- 参考文献列表、单条引用、BibTeX、RIS、Zotero item key 或论文参考文献页。
- 允许使用的数据源，例如 Crossref、PubMed、IEEE、CNKI、出版社页面或 Zotero。
- 是否需要生成可直接导入的修正文件。

**得到什么**

- 字段级核查表：原始值、可信来源值、差异和证据链接。
- 严重程度分级：必须修正、建议核对、仅供参考、无法验证。
- 可选 BibTeX patch、Zotero 更新建议或 Markdown 审查报告。
- 对不确定条目的人工核查清单。

**使用边界**

- 不会把单一搜索结果当作最终事实；关键字段优先回到 DOI、出版社或权威数据库。
- DOI、卷期和在线发表年份不一致时，会解释冲突而不是强行合并。
- 无法访问的数据库或中文来源会被标注为未验证。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-ref-verifier/README.md)

### 5. nature-literature-pipeline：持续跟踪新文献

多源发现、评分、筛选、摘要与本地归档。

**直接这样说**

> 使用 nature-literature-pipeline，先针对【主题】做一次过去 7 天的新论文筛选，候选最多 20 篇，精读前 3 篇并本地归档；本次不设置定时任务或对外推送。

**需要材料**

- 研究主题、关键词、排除词、重点期刊或重点作者。
- 推送频率、每次候选数量和最终精读数量。
- 输出位置，例如 Markdown 目录、飞书/Telegram 接口或本地归档文件夹。

**得到什么**

- 候选文献表和去重后的 Top 列表。
- 每篇重点论文的精读卡片：问题、方法、关键数据、局限和与你课题的关系。
- 可复用的管线配置、归档索引和失败/降级说明。

**使用边界**

- 自动推送依赖本机 cron、消息接口或用户配置的调度器。
- 无法访问全文时，会明确标注 `Abstract only` 或 `Metadata only`。
- 不会把评分当作论文质量的最终判断；高分候选仍需要人工阅读确认。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-literature-pipeline/README.md)

### 6. nature-reader：全文中英对照阅读

保留图文对应、公式和来源定位的 Markdown 阅读稿。

**直接这样说**

> 使用 nature-reader，把附件论文做成中英对照全文 Markdown，保留图表、公式和来源锚点，保存到【目录】，逐页处理。

**需要材料**

- PDF、DOI、arXiv 链接、出版社 HTML、题名或粘贴文本。
- 输出目录和是否需要图片裁剪。
- 是否保留英文原文、中文翻译、图表、表格和翻译备注。

**得到什么**

- `paper.md`：全文阅读材料。
- `source_map.json`：页码、文本块和图表来源映射。
- `translation_notes.md`：术语、无法确认内容和翻译说明。
- `assets/`：图表、裁剪图片和必要附件。
- `assets/equations/`：低置信度或图片化公式的原始裁剪（按需生成）。

**使用边界**

- 默认以 Markdown 为中心，不默认生成交互式问答面板。
- 扫描 PDF、双栏错序或版权受限全文可能需要额外人工校对；图片化公式会优先显示原图并标记转写置信度。
- 无法合法获取全文时，会基于可用摘要/元数据说明限制。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-reader/README.md)

### 7. nature-paper-xray：讲透论文的推理

理解研究起点、关键设计、可手算公式和证据边界。

**直接这样说**

> 使用 nature-paper-xray，精读附件论文，解释作者为什么这样设计，区分关键与可替代组件，为核心公式给出可手算例子，说明结论边界。

**需要材料**

- 论文本体：PDF、arXiv 编号或链接、出版社 HTML 页，或者直接粘贴正文。
- 附录和补充材料（有就一起给，附录里常有正文不放的消融和真实搜索范围）。
- 你的目的：只是读懂、要写相关工作、要审稿、还是要在组会上讲——这决定详细程度。
- 可选：论文的官方代码仓库。代码会暴露论文没写的归一化、预热、数据过滤，有时性能恰恰来自那里。

**得到什么**

一份 Markdown 长文，按这个顺序：

1. 论文真正主张什么（撇开它自己的宣传措辞）。
2. 还原出来的研究路径：卡在哪、押了什么、证据是什么。
3. 承重判定：逐个组件说明拿掉会不会塌，以及支撑这个判断的证据。
4. 关键公式的可算例子。
5. 证据边界：结果建立了什么、没建立什么。
6. 读完能带走什么、还有哪些问题开着。

**使用边界**

- **只读不判。** 它报告论文做了什么、证据够到哪儿，不评分、不排名、不判录用成熟度或新颖性——那是 `nature-reviewer`。
- 它不提炼写作范式，不产出可复用的行文模板。
- 它不做全文翻译或中英对照阅读。
- 它不检索文献、不核验引用、不替论文补引用。
- 它不代写正文。要写相关工作或做定位时，把读出来的东西交给 `nature-writing`。
- 论文没报告的事就写“论文没有报告”，不用常识补一个看着合理的数字。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-xray/README.md)

### 8. nature-paper-card：生成结构化精读卡

形成固定 01–16 节、有来源约束的 Paper Card。

**直接这样说**

> 使用 nature-paper-card，精读附件论文，生成中文完整 Paper Card，重点检查方法模块、关键实验、结论边界与可验证的后续研究想法。

**需要材料**

- 一篇论文的 PDF、DOI、arXiv 页面、出版社文章、粘贴文本，或已有的 `nature-reader` source map。
- 如有需要，说明输出语言、输出目录和希望重点审查的问题。
- 若只有摘要或局部材料，Skill 仍可运行，但会明确标记无法判断的部分。

**得到什么**

- `paper-card.md`：固定 01–16 节的深度 Paper Card。
- `source_bundle.json`：PDF 或 source map 的标准化来源包。
- `audit-report.json`：结构、定位和证据约束审计结果。
- 可选的 `rendered-pages/`：需要视觉核对时渲染的 PDF 页面。

**依赖与配置**

- 需要 Python 3。
- PDF 处理优先使用 Skill 自带脚本和当前环境中可用的 PDF 库。
- PDF 页码可靠时同时使用 PDF 页码和结构定位；页码提取失败时自动降级为结构定位，不伪造页码。
- source map 中缺失或非法的页码会保留为未定位块并给出警告，不会自动归入 PDF 第 1 页。
- 外部检索只用于文献背景核验、知识连接、书目信息确认或用户明确要求的新颖性检查。

**使用边界**

- 一次处理一篇论文，不负责批量文献监控。
- 不生成全文双语翻译；需要全文阅读材料时使用 `nature-reader`。
- 不生成正式同行评审报告；需要审稿人视角时使用 `nature-reviewer`。
- 不把 Paper Card 改写成公众号文章，也不生成第 17、18 节。
- 来源不足时明确写 `Not assessable`，不会补写不可见的实验或页码。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-card/README.md)

### 9. nature-paper-trans：保留版式的中文 PDF

逐页生图翻译，输出中文图片型 PDF。

**直接这样说**

> 使用 nature-paper-trans，翻译附件英文论文第 1–2 页，保留源页尺寸与版式，输出中文 PDF，按页顺序处理；术语表为【词表】。

**需要材料**

英文论文 PDF，以及可选的页码范围、术语表、保留名单或已确认译文。页码按从 1 开始的 **PDF 实际页序**计算，不按论文印刷页码计算；未指定范围时处理全文。

源 PDF 需清晰、可正常打开且未加密，不要求具备可提取的文字层。更新已有结果时，需提供原任务资料并明确要更新的原页码和要求。

**得到什么**

只交付一个中文 PDF：图片型，按原文页序排列；默认保留每个源页面的尺寸、方向和比例，图片在对应页面内等比例居中。只有用户明确要求时才统一转换为 A4。不生成或交付逐页检查 Markdown。

**依赖与配置**

需要支持内置 `image_gen` 的 Codex、Python 3.9+、PyMuPDF 和 Pillow。脚本支持 macOS、Linux、WSL2 以及原生 Windows；原生 Windows 使用 PowerShell，WSL2 使用 Bash。依赖清单见 [requirements.txt](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-trans/requirements.txt)。

在 Windows PowerShell 中，将示例里的 `$PYTHON` 替换为 `python` 或 `py -3`，并把路径写成带引号的 Windows 路径；流程和文件格式不变。原生 Windows 不要求额外安装 POSIX 文件锁库。

Python 脚本管理源页渲染、调用和检查记录、图片保存和 PDF 合并；脚本本身不调用生图服务，不判断译文是否正确。`--pdf-only` 省略检查说明附件，仍要求记录新生成图的检查。本技能独立运行，不依赖其他 Nature Skills 技能。

**使用边界**

- 输出不包含 OCR 文字层，不是可编辑 Word 或可搜索文本 PDF。
- 不承诺像素级 1:1 或逐字准确。生成结果可能存在错译、漏译、公式图表变化或局部版式偏差；基础对照不能代替逐字审校，关键数据与结论应对照原文。
- 确认缺页后，部分 PDF 标注实际包含的原页码；全部页面均无可用结果时不交付 PDF。
- 指定页更新失败时沿用已有可用结果。源 PDF 和已有成品不会被覆盖。

执行规则见 [SKILL.md](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-trans/SKILL.md)，翻译与版式要求见 [通用提示词](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-trans/references/image-translation-prompt.md)。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-trans/README.md)

### 10. nature-paper2ppt：论文变组会 PPT

根据论文内容重新组织中文汇报叙事。

**直接这样说**

> 使用 nature-paper2ppt，把附件论文做成 12 页中文组会 PPT，面向研究生，报告 15 分钟，保留关键原图和来源，附逐页讲稿。

**需要材料**

- 论文 PDF、DOI、arXiv 链接、出版社页面、摘要加图注或阅读笔记。
- 报告时长、听众背景、页数范围和是否需要 speaker notes。
- 是否必须保留原图、是否允许裁剪或重画示意图。

**得到什么**

- 可编辑 PowerPoint 文件。
- 图表资产清单和裁剪/引用说明。
- 每页标题、要点、takeaway 和 speaker notes。
- 包体检查结果，例如媒体嵌入、页数、备注和布局风险。

**使用边界**

- 不会把论文内容改写成无法回溯来源的泛泛介绍。
- 图像质量不足、PDF 扫描质量差或原图无法提取时，会说明替代方案。
- 如果任务是全文翻译或逐段阅读，优先使用 `nature-reader`。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper2ppt/README.md)

### 11. nature-image2ppt：截图变可编辑 PPT

还原已有页面的文字、形状、连线和布局。

**直接这样说**

> 使用 nature-image2ppt，把这 2 张幻灯片截图重建为可编辑 PPT，文字和流程图尽量用原生对象，复杂插图可保留图片，先检查依赖并报告渲染验证结果。

**需要材料**

- 幻灯片图片、扫描 PDF 或图片型 PPT/PPTX 文件。
- 希望保留的页面范围、语言、尺寸或字体要求；没有特殊要求时可省略。
- 是否允许复杂插图作为独立图片资产保留，以及材料是否必须离线处理。
- 如需在线生成或编辑图片资产，需明确允许上传当前任务的提示词和必要页面图片，并提供 Codex OAuth 或兼容 OpenAI Images API 的服务配置。

**得到什么**

- 对象级可编辑 PowerPoint 文件。
- 每页的 manifest、文字提示、渲染预览和 QA 报告。
- 最终文件验证结果，以及仍作为可替换图片资产保留的复杂视觉清单。
- 页面输出严格限制在各自页面目录，最终文件限制在本次 run 目录，并采用原子写出避免失败后留下半成品。

**依赖与配置**

- 使用 Python 3.10 或更高版本，并安装 `requirements.txt`。
- 复制或同步技能文件不会自动安装 Python 包；必须在实际运行 CLI 的同一 Python 环境中安装依赖，并以 `doctor --json` 成功为准。
- 使用 Microsoft PowerPoint（Windows）或 LibreOffice 完成渲染检查；以 `python cli/image2ppt/cli.py doctor --json` 的结果为准。
- 图片生成和编辑可使用 Codex OAuth，或通过 `openai-compatible-api` 配置任意兼容 OpenAI Images API 的 Base URL、API Key 和模型 ID；第三方端点不会收到 Codex OAuth 凭证。
- 在线文字识别使用百度 AI Studio `PADDLE_OCR_TOKEN`。将 `config.example.yaml` 复制为同目录的 `config.yaml` 后填写 Token；真实配置已被 Git 忽略，不能提交。
- 完整实现同步自 [Paul-Jeo/Image2PPT](https://github.com/Paul-Jeo/Image2PPT)，并在本技能目录中保留 MIT License。

**使用边界**

- 只还原已有页面；根据论文、提纲或笔记创作新 deck 时使用 `nature-paper2ppt`。
- 照片、复杂插画、密集知识图谱和难以稳定测量的视觉可能部分保留为图片资产。
- 低分辨率输入、缺失字体和复杂曲线会限制还原精度，需要根据渲染对照复核。
- 在线图片生成或编辑会把当前任务的提示词和必要页面图片发送到所选图片服务；敏感材料应选择离线模式或经批准的服务。
- 在线 OCR 会把当前任务页面发送到百度服务；敏感材料应选择离线模式。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-image2ppt/README.md)

### 12. nature-paper2word：学术稿件排版成 Word

Markdown 转学校或期刊规范的 Word，支持原生公式与三线表。

**直接这样说**

> 使用 nature-paper2word，把【稿件.md】按附件学校规范排成 Word，公式和表格保持可编辑，先检查排版引擎，保留原件并另存成品。

**需要材料**

- **稿件**：Markdown 文件。若手上是文字稿、PDF 或旧 `.docx`，先交给本技能整理成 Markdown，不改动原件。
- **格式要求**（可选）：一份文本文件，一行描述一种样式；不提供就用内置预设，按稿件语种自动选择。
- **文献**（可选）：`.bib` 文献条目。没有则文末不生成文献表，可在导出后用文献管理器插入。
- **场景信息**：中文还是英文，学位论文还是期刊投稿，目标期刊或学校名称。

**得到什么**

- 一个 `.docx`：公式为 Word 原生对象，三线表、题注、页码页眉、目录、文献表按格式要求生成。
- 导出前的检查结果：不符合稿件契约的地方带行号与改法；导出后的数值完整性与样式对账结果。
- 按需给出多个版式，同一份稿件共用一套内容。

**依赖与配置**

本技能只有文档，引擎是 PyPI 上的 `md-to-word-docx`，装一次即可，技能文件不随引擎版本改动。使用前先确认命令可用：

```bash
md-to-word --version
```

没有输出就安装 `pip install md-to-word-docx` 后重新检查。完整词表、契约细则与能力边界在包内手册，`md-to-word --contract` 会打印它的绝对路径。

**使用边界**

- 不做自定义封面、合并单元格、多栏排版、文字环绕图片；这些导出后在 Word 中补。
- 只支持公式的交叉引用；图与表的编号写在题注里。
- 目录页码与随章变化的页眉是 Word 域，打开时 Word 会询问是否更新。
- 不做 PDF、HTML、LaTeX 输出；不做幻灯片与基金申请书。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper2word/README.md)

### 13. nature-experiment-log：整理实验记录

图片、文字、语音转写整理成可追溯 Markdown 日志。

**直接这样说**

> 使用 nature-experiment-log，根据这些记录生成今天的实验日志，整理样品、条件、步骤、观察、异常和下一步，链接原附件，缺失信息单列，保存到【目录】。

**需要材料**

- 实验日期、样品、条件、处理步骤、观察结果或原始附件。
- 目标 vault / 输出目录；如果没有指定，技能会先生成可保存的 Markdown。
- 需要固定的命名规则、项目编号或样品编号。

**得到什么**

- 一条带 YAML frontmatter 的实验日志。
- 对原始图片、音频、表格或聊天记录的附件索引。
- 缺失字段清单和后续实验动作建议。

**使用边界**

- 不会替作者编造温度、时间、配比、设备型号或实验结果。
- 对无法从材料中确认的信息，会保留 `AUTHOR_INPUT_NEEDED` 或中文确认项。
- 核心流程不依赖飞书或 Obsidian；只有使用相应集成时，才需要本机 CLI、bot 权限或 vault 目录权限。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-experiment-log/README.md)

### 14. nature-statistics：检查统计报告

核对实验单位、重复、检验、效应量和跨章节一致性。

**直接这样说**

> 使用 nature-statistics，检查附件 Methods 和图注中的实验单位、独立重复、n、误差线、统计检验与多重比较，列出缺失事实并给出保守改写。

**需要材料**

- 样本量、重复层级、实验单位、分组、检验方法和多重比较方式。
- 图表、图注、Results 文本、统计输出或审稿意见。
- 哪些事实已确认，哪些需要保守标注。

**得到什么**

- 统计报告审查：主要问题、风险等级和需要作者确认的信息。
- 可粘贴的 Statistical analysis、Results 或 figure legend 改写。
- 跨章节统计一致性风险清单。
- 审稿统计问题的逐点回应草稿。
- `AUTHOR_INPUT_NEEDED` 清单，用于标记缺失样本量、检验或设计事实。

**使用边界**

- 不会替作者编造样本量、重复数、p 值、效应量、模型假设或检验名称。
- 不直接替代统计师或完整再分析；如需重新建模，应要求原始数据和分析代码。
- 不能仅凭图像判断实验单位和独立重复，需要作者确认设计。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-statistics/README.md)

### 15. nature-figure：制作与审查科研图

数据绘图、多面板证据组织、图件导出与布局审查。

**直接这样说**

> 使用 nature-figure，根据【数据文件】制作科研图，先明确每个面板要支持的结论，使用 Python，保留全部观测，输出可编辑矢量图及绘图脚本。

**需要材料**

- 原始数据、已有图、图注、论文 claim 或想表达的机制。
- 目标期刊、单栏/双栏尺寸、输出格式和是否需要 source data。
- Python / R 偏好；如果没有偏好，技能会先询问或沿用本机记录。

**得到什么**

- 可运行的 Python 或 R 绘图脚本。
- SVG/PDF/TIFF/PNG 等图件文件，优先保留可编辑矢量版本。
- 面板说明、source data 映射、排除计数、逐面板视觉审查表、alignment JSON/诊断 SVG、碰撞 JSON/诊断 PDF 和投稿前 QA 记录。
- AI 示意图任务中，输出概念草稿和需要人工重画/核实的元素列表。

**使用边界**

- 不会把 AI 生成图片当作真实实验结果或定量数据面板。
- 不会把内部可用的 AI 草稿自动称为可投稿终稿；两者分别判定。
- 不会凭空补统计检验、样本量、误差线含义或实验条件。
- 不会为了渲染方便静默抽样、忽略变量或删除不完整观测。
- 不会把自动校验通过当作视觉验收；对齐门只保证已声明的几何关系在容差内，最终交付仍需逐面板检查不确定性、标签碰撞、间距和显著性层级。
- 私有模板可以在本机使用，但不应在面向用户输出中暴露私有路径、文件名或来源。
- 第三方参考材料的版权和再使用条件以其来源及 `THIRD_PARTY_NOTICES.md` 为准；本仓库不额外授予这些文件的使用权。

自动碰撞审计需要 PyMuPDF：

```bash
python -m pip install -r skills/nature-figure/requirements.txt
```

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-figure/README.md)

### 16. nature-proposal-writer：开题与研究方案

先建立问题链、证据和章节契约，再起草或修改。

**直接这样说**

> 使用 researchwrite（nature-proposal-writer），基于【主题与材料】先建立开题报告的问题链、研究目标、证据缺口和章节框架，暂不扩写正文。

**需要材料**

- 研究主题、目标读者、拟投稿/申报类型和已有材料。
- 已确认的事实、数据、图表、参考文献或不能改动的表述。
- 希望输出的长度、语言和文件格式。

**得到什么**

- 论证架构、章节契约和写作顺序。
- 可粘贴的正文草稿或修订版。
- QA 结果：内容缺口、语言风险、引用/编号问题和需要作者确认的事实。

**使用边界**

- 不会替作者虚构实验结果、参考文献、合作基础或可行性证据。
- 对缺失事实会标记 `AUTHOR_INPUT_NEEDED`，而不是用流畅文字掩盖。
- 如果只是句子级英文润色，优先使用 `nature-polishing`。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-proposal-writer/README.md)

### 17. nature-social-science：社科选题与论证

研究兴趣收敛、文献版图、证据路线与可行性评估。

**直接这样说**

> 使用 nature-social-science，根据【研究兴趣】提出有边界的社科研究问题，结合【时间、数据、经费限制】审计新颖性与可行性，区分相关性和因果性主张。

**需要材料**

- 你的兴趣、宽泛主题或暂定研究问题（任选其一作为起点）。
- 你已经读过的关键文献、已有数据或方法偏好（如有）。
- 你的约束条件：时间、经费、数据访问、伦理边界、目标学位层次。

**得到什么**

- 一页搜索空间、领域版图、3–7 张未决问题卡。
- 1–3 条证据路线与每张候选 RQ 的候选卡（6–12 张）。
- 新颖性审计与 Reviewer 2 攻击记录、可行性档案、最多三张 Topic Cards 短名单。
- 论证段落的诚实表述修改建议与 red flags 清单。

**使用边界**

- 不替你生成一个"正确题目"，不保证新颖、录取、资助、发表或论文成功。
- 不把某种方法（定量、质性、因果推断等）当作高质量研究的默认答案。
- AI 的自信不是证据：不知道的一律写"未知"，不编造引文、来源或结果。
- 需要真人判断的环节（学科分量、资料获取、敏感参与者、导师意愿）会明确停下来，而不是替你决定。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-social-science/README.md)

### 18. nature-writing：起草和重构论文章节

由已确认的结果、图表与论点搭建手稿和首次投稿材料。

**直接这样说**

> 使用 nature-writing，根据这些图和已确认结果，先画出论点—证据映射，再起草英文摘要与引言，不添加未证实结论，缺失引用单独标记。

**需要材料**

- 核心 claim、图表、关键结果、实验事实和目标读者。
- 目标章节、长度、语言和需要保留的术语。
- 已确认引用、限制条件和不能新增的结论。

**得到什么**

- 章节大纲、claim-evidence map 或可粘贴正文。
- Results allocation table、删除/替换记录和主文压缩前后字数差（需要时提供）。
- 对 novelty、significance、证据链和读者路径的修改建议。
- 需要作者确认的事实、引用或图表说明。
- 首次投稿材料包、可编辑 LaTeX 模板、缺失信息清单和 `ready / ready_with_author_checks / blocked` 状态。

**使用边界**

- 不会替作者虚构实验结果、统计意义、机制解释或参考文献。
- 如果已有英文草稿只需要句子级润色，优先使用 `nature-polishing`。
- 如果需要先找文献支撑 claim，优先使用 `nature-citation` 或 `nature-academic-search`。
- 首次投稿材料由本技能处理；返修 cover letter、rebuttal 和逐点回复由 `nature-response` 处理。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-writing/README.md)

### 19. nature-polishing：润色与学术翻译

保留科学含义，改进英文、逻辑及术语一致性。

**直接这样说**

> 使用 nature-polishing，把下面段落润色为 Nature 风格英文，保留数值、术语与结论强度，给出修改稿和主要改动理由：【段落】。

**需要材料**

- 原文、目标章节、论文类型和希望保留的术语。
- 不能改变的事实、数据、引用和专有表达。
- 期望输出：只给改写版，还是给修改说明和风险标记。

**得到什么**

- 可粘贴的英文改写或中英对照版本。
- 关键修改说明：逻辑重排、语气收敛、术语统一和声称边界。
- 全文一致性风险清单；机械扫描结果逐条回到上下文确认后再修改。
- 主文压缩任务可附结果分配表、删除记录、统计位置记录和 claim repetition map。
- 需要作者确认的事实或引用意图。

**使用边界**

- 不会替作者新增结果、机制、统计意义或未给出的引用。
- 不会为了更像 Nature 而夸大 novelty、causality 或 generality。
- 如果需要从零搭建论文章节，优先使用 `nature-writing`。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-polishing/README.md)

### 20. nature-reviewer：投稿前模拟审稿

独立评审、Major/Minor 问题、证据定位与后置综合。

**直接这样说**

> 使用 nature-reviewer，从目标期刊【名称】的审稿角度评估附件手稿，按技能要求独立形成三份评审，再做综合，指出每项问题的证据位置与解决判据；考虑 8GB 内存，按顺序运行。

**需要材料**

- 手稿全文、摘要、关键章节、图表、图注或作者说明。
- 目标期刊、学科领域和你最担心的审稿风险。
- 已有补充实验或不能新增实验的限制。

**得到什么**

- 三份 peer-review style reports。
- Cross-review synthesis：共识问题、分歧重点和编辑层风险。
- 带稳定编号、claim pointer、evidence pointer 和解决判据的可追溯审稿意见。
- 分级的 Major/Minor 意见、Blocking 风险和去重后的 minor revision checklist。
- 必须补强的实验、分析、叙事或图表证据清单。
- 对无证据判断的明确标记。

**使用边界**

- 不会虚构具体审稿人身份、专业人设或编辑决定。
- 不同 reviewer 之间不能读取、引用、赞同或回应彼此的意见；综合判断只在全部独立报告锁定后生成。
- 只基于用户提供材料和技能内官方审稿规则做保守模拟。
- 如果目标是写返修回复，优先使用 `nature-response`。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-reviewer/README.md)

### 21. nature-response：回复真实审稿意见

编辑邮件解析、逐点回应、修改清单和返修材料。

**直接这样说**

> 使用 nature-response，根据编辑邮件、审稿意见和实际完成的修改，生成逐点英文回复及返修 cover letter；未完成实验和缺失行号明确标记，不写成已经完成。

**需要材料**

- 编辑决定信、审稿意见、返修要求或已有 rebuttal 草稿。
- 若决定信未明确说明，请告知这是 Major Revision（大修）还是 Minor Revision（小修）。
- 已完成或计划完成的实验、分析、图表、行号和手稿修改位置。
- 目标期刊、稿件号、题名和提交材料要求。

**得到什么**

- Response strategy summary。
- 给每位审稿人分别生成的逐点回复信、返修 cover letter 或 LaTeX response package。
- 供作者或编辑核对的总表，明确标记为不面向审稿人。
- 手稿修改清单、缺失信息清单和风险提示。
- 带任务状态、所需输入、预期产物和是否阻塞最终提交的逐条 tracker。
- 可选标红修改稿摘录；原文修改必须基于作者提供的文本。
- 返修包机械一致性报告；编译页码、颜色、引用和参考文献仍需在最终 PDF 中核验。

**使用边界**

- 不会编造实验、分析、行号、图版、统计结果或编辑要求。
- 不会在某位审稿人的回复中写“另一位审稿人也提出了”或“见我们对 Reviewer 2 的回复”等交叉信息。
- 不会用“我们已经在文章中说明”责备审稿人，而会直接回答、进一步澄清并标明修改后的具体位置。
- 不会把主文写成预防性 reviewer response，也不会把非核心稳健性和解释性递归不断追加到 Results。
- 对需要作者确认的信息会用中文标记，而不是直接写成事实。
- 如果任务是模拟投稿前审稿意见，优先使用 `nature-reviewer`。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-response/README.md)

### 22. nature-data：数据与代码可用性说明

数据仓储、可用性声明、来源映射和 FAIR 清单。

**直接这样说**

> 使用 nature-data，根据这份数据清单和真实访问限制，起草英文 Data Availability，并检查 DOI、accession、许可证与缺失信息，不替我上传数据。

**需要材料**

- 支撑每个图表或结论的数据来源。
- 数据是否已上传、仓储链接、accession、DOI、embargo 或访问限制。
- 代码、材料、实验方案和第三方数据的可用性边界。

**得到什么**

- 可粘贴的英文 Data Availability statement。
- 数据集到图表/结论的映射表。
- 缺失信息清单和 FAIR / DataCite 元数据检查。
- 对受限数据、第三方数据或补充材料数据的保守表述建议。

**使用边界**

- 不会编造 accession、DOI、许可证、仓储记录或访问限制。
- 信息缺失时，会给出可用草稿和短确认清单，而不是假装完整。
- 受伦理、隐私、商业或第三方协议限制的数据，需要作者提供真实限制条件。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-data/README.md)

### 23. nature-paper-to-patent：论文与技术资料转专利草稿

挖掘技术贡献，形成技术交底书、权利要求与证据映射。

**直接这样说**

> 使用 nature-paper-to-patent，从附件论文提取候选技术贡献，先生成技术交底书框架和证据缺口清单，不编造实施例；需要查新时先说明检索范围。

**需要材料**

- 论文 PDF、技术报告、代码、图表、实验记录或发明人补充说明。
- 希望保护的对象：方法、系统、装置、材料、工艺或软件流程。
- 已知现有技术、不能公开的信息和必须保留的术语。

**得到什么**

- 技术问题、技术方案、实施链条和有益效果分析。
- 技术交底书 Markdown / Word，含查新结论、系统框图、流程图、公式与参数一致性自检。
- 权利要求草稿及每个特征的证据映射。
- 说明书、摘要、附图说明和黑白流程图。
- 可选 DOCX、SVG、PNG 和审阅报告。

**依赖与配置**

- 完整功能依赖技能目录中的 `manifest.yaml`、`static/`、`references/`、`scripts/` 和 `requirements.txt`。
- 需要生成 DOCX、公式或流程图时，会使用本机 Python 依赖和脚本。
- 交底书分支的 Office 转换、Mermaid 渲染、国知局查新脚本位于 `scripts/disclosure/`；可选国知局检索依赖见 `scripts/disclosure/requirements-cnipa.txt`。

**使用边界**

- 这是技术起草辅助，不替代专利代理师或法律意见。
- 不会虚构实施例、实验数据、权利要求特征或现有技术对比。
- 证据不足的特征会被标记为缺口，而不是写进主权利要求。

[上游完整说明](https://github.com/Yuan1z0825/nature-skills/blob/c1637a89c7097d486ba1c6e755e34d01cbb24998/skills/nature-paper-to-patent/README.md)

### 24. nature-shared：共享支持包

保存术语表、论文类型、伦理、期刊格式、一致性审查等公共参考，供其他技能按需读取。无需独立提示词，也不需要启动任何服务；保持与其他技能同级即可。

## 推荐的日常工作流程

1. **入门读论文**：academic-search 找到目标 → downloader 获取合法全文 → reader 全文对照 → paper-xray 讲懂难点 → paper-card 留下精读笔记。
2. **准备组会**：提供论文、报告时长和听众 → paper2ppt；只有现成截图需要还原时才用 image2ppt。
3. **开展研究并写论文**：experiment-log 记录原始信息 → statistics 检查统计报告 → figure 制图 → writing 起草 → polishing 润色 → citation 补引用 → ref-verifier 核验 → reviewer 检查投稿风险。
4. **投稿与返修**：data 准备数据说明；writing 准备首次投稿材料；收到真实审稿意见后用 response；需要 Word 时用 paper2word。

不必一次跑完整条流程。只有论文摘要时，要明确要求标注材料范围，不能据此声称已检查全文实验。

## 8GB 内存电脑的使用建议

- 技能文件本身是指令、参考资料、脚本和素材；安装不等于在后台运行 24 个程序。
- 每次一篇论文或一个技能，避免一口气让整套技能连续处理资料库。全文转译、PPT 渲染和生图按页/按批处理，优先保留可复用中间结果。
- 先用 reader 或 paper-card，只有确实需要保留页面外观时再用 paper-trans。图片生成可能额外消耗额度，且图片 PDF 通常比纯文本结果大。
- image2ppt 可能需要额外 OCR 与渲染工具；paper2word 依赖 md-to-word-docx；figure 按实际选择 Python 或 R；不用的工具不预装。
- literature-pipeline 先单次运行验证结果，只有明确要求定期执行时才设置自动化。安装本身未启用推送、定时器或自动更新。
- 先明确输入文件、页数和结果长度，避免重复读取全文或反复渲染。不同任务可复用 reader 的 source map。
- 在线 OCR 或图片服务的材料上传范围，要在实际使用时按选定服务说明确认；凭据只做本机安全配置。

## 更新与排错

- **找不到技能**：下一轮明确指定技能名；若仍未识别，开启新聊天，核对安装目录内的 SKILL.md。researchwrite 使用实际声明名。
- **缺依赖**：技能已安装与执行环境就绪是两件事。让 Codex 检查当前任务所需依赖，优先复用已有运行环境，不批量安装所有包。
- **无法下载或检索**：检查合法访问权限、网络和对应数据源配置；不会因安装技能而获得数据库订阅。
- **更新**：告诉 Codex“检查 nature-skills 上游更新，与本次清单比较后更新，保留本地改动”。本次由 Skill Installer 手动安装，没有 npx 管理记录，不能假定 npx skills update 能管理本次安装。
- **卸载**：删除明确选定的技能目录即可；卸载共享包前先确认没有技能继续依赖它。科研原始材料和成果在独立输出目录中保留。

## 文档依据

本指南依据固定提交中的根 README、各技能 README 与安装文件整理，调用示例为中文改写。上游对 Stable/Beta/Draft 的标签是作者自述，不等于本机已完成所有功能测试。安装核验检查文件完整性，不代表外部服务或每条工作流均已跑通。
