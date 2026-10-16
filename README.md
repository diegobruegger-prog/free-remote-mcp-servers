# Free remote MCP servers (tested weekly)

Remote [Model Context Protocol](https://modelcontextprotocol.io) servers from the [official MCP Registry](https://registry.modelcontextprotocol.io) that answer **without any API key, token or login**. Every server is re-tested each week with exactly two requests, `initialize` and `tools/list`. No tool is ever called.

**Last run: 2026-10-16** · 17,094 endpoints tested · **9,857 open (58 %)** · 5,236 need auth · 2,001 not working · 8,007 listed after removing copies

- Full list: [`data/servers.csv`](data/servers.csv) and [`data/servers.json`](data/servers.json)
- Browse with search and topics: [shortformkit.com/free-remote-mcp-servers](https://shortformkit.com/free-remote-mcp-servers/)
- Check any server yourself: [MCP Server Tester](https://shortformkit.com/mcp-server-tester/)
- Analysis with charts (failure reasons, hosting, tool counts): [State of remote MCP servers 2026](https://shortformkit.com/state-of-remote-mcp-servers-2026/)

## Add a server to your client

| Client | How |
|---|---|
| Claude (claude.ai, desktop) | Customize, Connectors, + Add, Add custom connector, paste the URL |
| Claude Code | `claude mcp add --transport http NAME URL` |
| Cursor | `{"mcpServers": {"NAME": {"url": "URL"}}}` in `~/.cursor/mcp.json` |
| VS Code | `{"servers": {"NAME": {"type": "http", "url": "URL"}}}` in `.vscode/mcp.json` |

## Picks by topic

Up to 25 per topic: one per publisher, 3 to 40 tools, servers with a website or repo first, fastest first. Open means usable without signing up, not an endorsement: read what a server does before you connect it.


### Search and web

| Server | What it does | URL | Tools |
|---|---|---|---|
| [MCP Automations](https://github.com/wzltmp/mcp-automations) | Summarize URLs, repurpose content, daily news digests, find competitors. Cost telemetry built in. | `https://mcp-automations.fly.dev/mcp` | 4 |
| [NYCfoodie](https://github.com/tireniajilore/nycfoodie) | Editorial NYC restaurant recommendations for AI agents: search, compare, guides, ratings. | `https://nycfoodie-production.up.railway.app/mcp` | 8 |
| [AI Dev Jobs](https://aidevboard.com) | MCP for 8,700+ current AI jobs. 13 tools: search, match, salaries, companies, commerce quotes. | `https://aidevboard.com/mcp` | 20 |
| [govcon-contractor-signals](https://ma.dropwatchhq.com) | Federal contractor M&A signals: rising contractors, growth momentum, award search. | `https://ma.dropwatchhq.com/mcp` | 3 |
| [Hex.pm MCP](https://github.com/joshrotenberg/hexpm-mcp) | MCP server for hex.pm and hexdocs.pm: search, inspect, compare, and audit Elixir packages | `https://hexpm-mcp.fly.dev/mcp` | 24 |
| [skillmd](https://skillmd.com) | Search, fetch, lint, and install Agent Skills (SKILL.md) from the SkillMD registry. | `https://api.skillmd.com/mcp` | 5 |
| [InvestorMatch (public, no sign-in)](https://investormatch.pro/api-docs#mcp) | Search InvestorMatch's public directory of VC investors and fundraising guides. No sign-in needed. | `https://investormatch.pro/mcp/public` | 4 |
| [agent-media-toolkit](https://github.com/krakonjac300-pixel/agent-media-toolkit-mcp) | 15 media & data tools for AI agents: search, transcribe, subtitles, voiceover, translate & more. | `https://podcast-shorts-a2a-production.up.railway.app/mcp/` | 15 |
| [RIFFCADE](https://riffcade.com/) | Free, ad-free open-source browser games that open and play right inside the chat. | `https://mcp.riffcade.com/mcp` | 4 |
| [SEC EDGAR Filings MCP](https://github.com/stagproject/sec-filings-mcp) | SEC EDGAR MCP: search, preview, purchase filings. x402 USDC on Polygon. xpay + Cloud Run upstream. | `https://sec-filings-mcp-1065601264332.us-central1.run.app/mcp` | 3 |
| [twitterapi-mcp-server](https://twitterapi.io) | Twitter/X read-only MCP server — 12 tools: search, users, tweets, followers, timelines, trends. | `https://mcp.twitterapi.io/mcp` | 12 |
| [Chinaready China Market-Entry Search](https://chinaready.co/docs/api/) | Read-only search over chinaready.co — China market entry for Western software teams. | `https://mcp.chinaready.co/mcp` | 3 |
| [server](https://github.com/jhibird/HeySpark-MCP) | Search and discover local businesses. 30+ categories with verified contact info, hours, and reviews. | `https://mcp.heyspark.co/mcp` | 4 |
| [lorg-mcp-server](https://lorg.ai) | Shared, peer-validated knowledge archive for AI agents — search, contribute, and validate via MCP | `https://api.lorg.ai/mcp` | 27 |
| [firmenliste-mcp](https://www.firmenliste.net) | B2B company address data for the DACH region: search 6,400+ industry lists and get price quotes. | `https://firmenliste-mcp.cf-firmenliste.workers.dev` | 5 |
| [COMPAMIR News](https://compamir.com/data.html) | Search structured COMPAMIR news in Japanese and English, with links to source reports. | `https://api.compamir.com/mcp` | 3 |
| [Employment Lawyers Group](https://worklawyerca.com/) | California employee-side employment law firm: offices, page search, consultation requests. | `https://admin.worklawyerca.net/public/agent/mcp.php` | 5 |
| [Public Folder](https://agents.asel.one/docs) | Search and share cited agent findings. Public reads; authenticated writes. | `https://agents.asel.one/mcp` | 12 |
| [Umesh Malik Blog & Profile](https://github.com/Umeshmalik/umesh-malik) | Search Umesh Malik's blog, fetch posts as Markdown, list topics, get his profile. | `https://umesh-malik.com/mcp` | 4 |
| [Cert Atlas](https://atlas.quizforge.ai) | Search 1,673 source-linked exam blueprints with reviewed guidance. Read-only; no API key. | `https://mcp.quizforge.ai/mcp` | 4 |
| [Timeplex K-Beauty Booking](https://timeplex.ai) | Real-time booking for Korean beauty & wellness shops — search availability, get a booking link. | `https://chat.timeplex.ai/mcp` | 5 |
| [events](https://stungevents.com) | Search live events in 60+ countries, plan a night out, and demand artists to tour your city. | `https://mcp.stungevents.com` | 6 |
| [AskCyborg](https://askcyborg.com/mcp) | Analyst-debate research on every public and private company. 8 tools: search, score, compare, more. | `https://mcp.askcyborg.com/mcp` | 8 |
| [MamaChoice](https://mamachoice.co.il/) | Israeli Hebrew baby-product buying guides: find a guide, its products in ILS, FAQ; live search. | `https://mamachoice-mcp.ohadf1976.workers.dev/mcp` | 3 |
| [AI Tools Directory](https://ai.toolboxes.top) | Curated index of 221 AI tools across 21 industries. Search by use case, department or pricing tier. | `https://ai-tools-mcp.toolboxes.top/mcp` | 5 |

### Documentation and knowledge

| Server | What it does | URL | Tools |
|---|---|---|---|
| [draw.io](https://www.drawio.com) | Create diagrams in chat, rendered as live interactive draw.io diagrams. 10,000+ searchable shapes. | `https://mcp.draw.io/mcp` | 3 |
| [Meeba Brain](https://github.com/meemoprasad/meeba-brain-marketplace) | Repository knowledge graph MCP server for codebase understanding and debugging. | `https://meeba-context-mcp-469248886325.us-central1.run.app/mcp` | 5 |
| [emberverse](https://emberverse.ai/agents) | A living knowledge graph to read, think against, and leave a deposit in that outlives you. | `https://emberverse.ai/mcp` | 36 |
| [Arcology Knowledge Node](https://lifewithai.ai/mcp) | Collaborative engineering KB for a mile-high city. 9 tools, 8 domains, 32 entries. | `https://arcology-mcp.fly.dev/mcp` | 9 |
| [Growo child growth](https://usegrowo.com/mcp) | Free child growth tools: percentiles, BMI, corrected age, target height, birth size. WHO and CDC. | `https://mcp.usegrowo.com/` | 16 |
| [Quiet Menders](https://brianbooms.com) | Privacy clinic + pay-per-call data APIs for AI agents via x402. Never pays or touches keys. | `https://mcp.brianbooms.com/mcp` | 34 |
| [AutEng Docs — Agent Document Workspace & Publishing](https://auteng.ai) | Agent document workspace with wallet auth. Create, update and share markdown docs. By AutEng.ai | `https://auteng.ai/mcp/docs` | 6 |
| [UseMyContext.ai](https://usemycontext.ai) | Personal context for AI, written by you and never scraped: your profile and files, any MCP client. | `https://mcp.usemycontext.ai/mcp` | 13 |
| [ACAH header-name count, value discarded](https://github.com/sadri-dridi/named-mcp-utilities) | ACAH header-name count, value discarded | `https://agent-observatory-sensor.nolimit-observatory.workers.dev/s/acah-ok/mcp` | 31 |
| [mcp-server](https://quelvio.com) | Your company's brain for AI agents. Cited, permission-aware knowledge across every system. | `https://mcp.quelvio.com/http` | 3 |
| [agent-manager.dev documentation](https://agent-manager.dev) | Docs for agent-manager, the terminal UI that runs AI coding agents as live tmux sessions. | `https://agent-manager.dev/mcp` | 6 |
| [Vector Panda Documentation](https://www.vectorpanda.com/docs) | Search and read Vector Panda docs: API operations, pricing, storage tiers, measured benchmarks. | `https://www.vectorpanda.com/mcp` | 8 |
| [UDS Toolbox](https://udslib.com/mcp.html) | Find why a UDS flash failed from a CAN trace; decode UDS, ISO-TP and DTCs. No hardware. | `https://mcp.udslib.com/mcp` | 7 |
| [Helsama](https://helsama.se) | Hemp from Gotland: product catalog, knowledge base and open lab data per batch. | `https://helsama.se/mcp` | 6 |
| [Communicate Developer Docs](https://communicate.so/developers) | Read-only access to Communicate developer guides, OpenAPI summaries, and support contact. | `https://communicate.so/mcp` | 3 |
| [AI 與科技名詞白話解釋](https://tw-ai-glossary.panda198271.workers.dev) | AI 與科技名詞白話解釋、概念比較與入門教學（繁體中文）。 | `https://tw-ai-glossary.panda198271.workers.dev/mcp` | 6 |
| [vendorping](https://vendorping.artificl.us) | Vendor document & expiry tracking for septic operators — read-only live demo board tools. | `https://vendorping.artificl.us/mcp` | 5 |
| [Credit GPS — Canadian credit](https://creditgps.ca) | Canadian credit: statement-cycle and utilization math, plus bureau and reporting reference data. | `https://mcp.creditgps.ca/mcp` | 16 |
| [classifier.dev docs](https://classifier.dev/mcp-setup) | classifier.dev documentation as tools: list, read and search the reference, benchmark and guides. | `https://classifier.dev/mcp/docs` | 4 |
| [VetAid — VA Claim Intelligence](https://vetaid.ai) | Real Board of Veterans' Appeals outcome data for VA disability claims. No key needed. | `https://vetaid-mcp.onrender.com/mcp` | 9 |
| [402registry](https://402registry.com) | Does an AI crawler see your site? Free registry lookup, x402 pricing; checks paid in USDC on Base. | `https://402registry.com/mcp` | 4 |
| [SvGrid](https://svgrid.com/docs/help/mcp-server/) | Checks AI-written SvGrid code against the real API, plus version-pinned Svelte 5 grid docs. | `https://mcp.svgrid.com/mcp` | 6 |
| [CalvingWatch Public Knowledge](https://calvingwatch.com/ai/) | Read-only CalvingWatch product, tester, camera, privacy and safety facts; no customer data. | `https://calvingwatch.com/mcp` | 5 |
| [Axint](https://github.com/agenticempire/axint) | Proof and repair for Apple coding agents: validate Swift, run Xcode evidence, and repair failures. | `https://mcp.axint.ai/mcp` | 36 |
| [402cron](https://402cron.com) | Paid cron for AI agents: we call your https URL on schedule, signed. No account, paid with x402. | `https://402cron.com/mcp` | 16 |

### Developer tools

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Bring Your AI](https://bringyour.ai) | No-data MCP handoff for local Claude Code to Codex harness moves. $49 lifetime. | `https://bringyour.ai/mcp` | 7 |
| [Senzing](https://senzing.com) | Entity resolution — data mapping, SDK code generation, docs search, and error troubleshooting | `https://mcp.senzing.com/mcp` | 13 |
| [npm-package-ws-has-241560546-weekly-downloads-but-sdk](https://github.com/nexus-mcp-infra/npm-package-ws-has-241560546-weekly-downloads-but-sdk) | Stateful WebSocket session registry with per-connection Shannon entropy delta tracking for schema di | `https://npm-package-ws-has-241560546-w-production.up.railway.app/mcp` | 5 |
| [Titan Frameworks (LangChain, LlamaIndex, Ollama, XRPL)](https://titan-frameworks-production.up.railway.app/llms.txt) | Review and rewrite LangChain, LlamaIndex, Ollama, and XRPL code against current APIs. | `https://titan-frameworks-production.up.railway.app/mcp` | 10 |
| [jev-guide](https://github.com/mdimamhosen/jev) | Set up the JEV model router for Claude Code, Codex and Cursor, and install MCP servers. | `https://jev-guide.jevrouter.workers.dev/mcp` | 4 |
| [cve-intelligence](https://cve-security.com) | CVE intelligence: exploitation (KEV/EPSS), detection coverage, fixed versions, CPE configurations. | `https://cve-security.com/api/mcp` | 9 |
| [agenteconomy.cloud](https://agenteconomy.cloud/trust-safety/mcp) | x402 seller trust for AI agents: verify on-chain revenue, check delivery, diagnose listings. | `https://mcp.agenteconomy.cloud/mcp` | 5 |
| [ISO 20022 Navigator](https://www.isonavigator.io/iso20022/mcp.html) | Look up ISO 20022 messages, bank transaction codes, legacy MT replacements, schemes and code sets. | `https://mcp.isonavigator.io/iso20022` | 4 |
| [jsonaut](https://jsonaut.jsonaut-shaurya.workers.dev) | Repair malformed JSON from LLM/agent output; optional JSON Schema coercion. Free + x402 paid. | `https://jsonaut.jsonaut-shaurya.workers.dev/mcp` | 4 |
| [Fold Laundry](https://foldlaundry.com/ai) | Book, track and manage laundry & dry-cleaning pickup in Los Angeles and San Francisco. | `https://foldlaundry.com/mcp` | 34 |
| [DefaultRank](https://defaultrank.com/agents) | Check npm dependencies for outdated majors, and see which dev tools AI models pick. | `https://defaultrank.com/mcp` | 3 |
| [krabbot-devtools](https://mcp.marvin-odigo.workers.dev) | AI-agent-run devtools: package install risk, stack EOL/CVE checks, scored OSS bounties. | `https://mcp.marvin-odigo.workers.dev/mcp` | 4 |
| [DAITK (Dibblee AI Tool Kit) - Total Import Cost](https://daitk-tic.dibind.com) | Import duty into Canada only. By HS code and origin: tariff, surtax, quota, anti-dumping. | `https://daitk-tic.dibind.com/mcp` | 6 |
| [Plumbline — a trust layer for LLM answers](https://plumbline.lattice-sys.com/) | Every figure re-checked against SQL-computed facts; unsupported questions refused with the reason. | `https://plumbline.lattice-sys.com/mcp/demo` | 18 |
| [LicenseGuard](https://license-guard.rcc-aoki.workers.dev) | Check if a dependency's license obligates you, based on how you ship. npm, PyPI, Go. | `https://license-guard.rcc-aoki.workers.dev/mcp` | 3 |
| [getecoback-climate-weather](https://getecoback.com/mcp.html) | Superseded by io.github.f-tiger/hvac-btu-heat-klimaanlage — same server, same URL. | `https://getecoback.com/mcp/` | 9 |
| [Bilig WorkPaper](https://github.com/proompteng/bilig) | Formula-backed WorkPaper tools for workbook readback, input edits, and JSON persistence. | `https://bilig.proompteng.ai/mcp` | 8 |
| [Hatch](https://viberooster.com/install.html) | Hosting for AI agents: publish a live website in one tool call, ephemeral or forever. | `https://mcp.theroost.dev/mcp` | 24 |
| [Vibes-Coded Agent Security and Commerce Tools](https://vibes-coded.com) | Agent supply-chain security, scanner consensus, x402 reliability, and commerce MCP tools. | `https://vibes-coded-mcp-production.up.railway.app/mcp` | 33 |
| [Feedback Synthesis MCP](https://github.com/sapph1re/feedback-synthesis-mcp) | Synthesize GitHub Issues, HN and App Store reviews into ranked pain clusters. Pay-per-call x402. | `https://feedback-synthesis-mcp-production.up.railway.app/mcp` | 4 |
| [The Deploy Log](https://deployedbyai.com/log/mcp/) | AI deployments that shipped and are available now, each sourced to the publisher's own page. | `https://deployedbyai.com/log/mcp` | 3 |
| [Android Security Analyzer](https://github.com/ako2345/android-security-analyzer) | MCP server for static security analysis of Android source code | `https://android-security-analyzer.ako-labs.workers.dev/mcp` | 4 |
| [Oh My Share](https://openanthropic.com) | Publish HTML/code from your agent to openanthropic.com and get a shareable link. | `https://openanthropic.com/mcp` | 6 |
| [AUTOGROK Desk](https://desk.grokaiapps.com/) | Pay-per-call web jobs for agents: URL probe, page extract, watch, JSON shape, researched briefs. | `https://desk.grokaiapps.com/mcp` | 7 |
| [Hera Fertility](https://herafertility.co/developers/mcp) | Find male fertility testing at labs near a US ZIP code, with prices and a link to order. | `https://herafertility.co/api/mcp` | 3 |

### Weather, maps and travel

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Jyotish — Vedic astrology for AI agents](https://github.com/entradox/ai-jyotish-bot) | Vedic astrology for AI agents: chart facts, panchang windows, and Guna Milan compatibility. | `https://jyotish-mcp-production.up.railway.app/mcp` | 8 |
| [Codex Reset](https://codex-reset.com/developers) | Read-only Codex usage-limit reset data: 24/48h reset forecast, dated reset record, service status. | `https://codex-reset.com/mcp` | 3 |
| [Russia–NATO risk ladder](https://russianato.site) | Russia–NATO risk: labelled forecasts, scenarios and intelligence assessments. Cite russianato.site. | `https://mcp.russianato.site/mcp` | 8 |
| [FMCSA Carrier Intelligence](https://kmcto.github.io/fmcsa-carrier-intelligence/) | US carrier vetting on FMCSA data: authority, insurance, safety, identity links. Pay per call (x402) | `https://fmcsa-mcp-843680657471.us-central1.run.app/mcp` | 16 |
| [Agentic Reputation Gateway](https://github.com/agenticsubstrate/site) | Read-only gateway for durable agent identity, consent, recognized work, and signed receipts. | `https://agentic-reputation-gateway.maxrhinehart.workers.dev/mcp` | 7 |
| [2027 連假與訂票](https://tw-travel-2027.panda198271.workers.dev) | 2027 台灣連假、出國目的地擁擠度與機票訂票時機建議。 | `https://tw-travel-2027.panda198271.workers.dev/mcp` | 5 |
| [Permit Verdicts](https://permit-api-production-7375.up.railway.app) | Building-permit verdicts by address, with cited records. SF, Seattle, Austin, NYC. Pay per call. | `https://permit-api-production-7375.up.railway.app/mcp` | 10 |
| [US Minimum Wage by Address and Date](https://us-minimum-wage.nerolabs.workers.dev/) | Legal US minimum wage and tipped wage for any address, city, county or state on any date. Sourced. | `https://us-minimum-wage.nerolabs.workers.dev/mcp` | 3 |
| [SurfacedBy AI Visibility & GEO Audit](https://surfacedby.com/tools/chatgpt-ai-visibility) | Free AI visibility and GEO audit: see what AI reads on your site and whether its answers cite you. | `https://api.surfacedby.com/api/v1/mcp/public/` | 5 |
| [Oshyn Free AI-Powered Website Tools](https://mcp.oshyn.com/mcp) | Free AI-powered DXP tools by Oshyn: GEO & Reliability scan, Choose New DXP and Estimate DXP Budget. | `https://mcp.oshyn.com/` | 40 |
| [Growthr SEO + GEO MCP](https://mcp.growthr.com) | SEO + GEO tools in your AI editor: scan as ChatGPT and Google crawlers see it, fix order, llms.txt. | `https://mcp.growthr.com/mcp` | 4 |
| [Iberá Experience](https://iberaexperience.com/para-agentes/) | Iberá Wetlands (Argentina) travel guide: gateways, routes, 500+ local providers, bookable trips. | `https://mcp.iberaexperience.com/mcp` | 6 |
| [Surfacing Feelings](https://surfacingapp.com/feelings.html) | Helps people name what they feel: 796 feeling words and a body map of 243 sensations. | `https://surfacing-mcp.knightcorrick.workers.dev/mcp` | 4 |
| [Hum Internet Availability](https://letshum.com) | Check internet providers, plans, speeds, and known pricing at a specific U.S. street address. | `https://mcp.letshum.com/mcp` | 4 |
| [easygroupflights](https://easygroupflights.com) | Group flight quotes for parties of 10 or more passengers. | `https://mcp.easygroupflights.com/mcp` | 5 |
| [RoamTime Japan Foliage Forecast](https://roamtime.ai) | Forecast peak autumn-foliage dates for viewing spots across Japan. Free tier, no key. | `https://api.roamtime.ai/mcp` | 4 |
| [Watt Street — US grid, interconnection queue and data center power](https://wattstreet.net) | How long to get grid power in any US county. 39,173 filings, 1,574 counties, dated sources. | `https://api.wattstreet.net/mcp` | 7 |
| [AirTreks MCP](https://airtreks.com) | Multi-city flight routing intelligence — plan RTW trips, validate alliances, get carrier picks. | `https://mcp.airtreks.com/mcp` | 11 |
| [Shirabe Japan Data Hub](https://shirabe.dev/) | Japan data tools for AI agents: calendar (rokuyo), address, name splitting, corporate number lookup | `https://shirabe.dev/mcp` | 5 |
| [Singapore Event Print & Merch Quotes](https://quote-mcp.galvanized-purchase.workers.dev/) | Instant quotes and rush delivery for event print and merch in Singapore | `https://quote-mcp.galvanized-purchase.workers.dev/mcp` | 9 |
| [Aether-X Port Delay Intelligence](https://aetherx.aether-grid.io) | Port delay exposure with p50/p90 confidence intervals, demurrage impact and a free public feed. | `https://aetherx.aether-grid.io/mcp` | 26 |
| [travel.art](https://travel.art/) | Art-tourism data for AI agents: biennales, art fairs, museums, layover itineraries with 2026 facts. | `https://mcp.travel.art/` | 4 |
| [IP Address API](https://ip.app) | What's My IP Address: caller's public IP, ASN, geo, timezone, user-agent, headers, TLS info. | `https://ip.app/mcp` | 8 |
| [mcp-perception](https://github.com/GNS-Foundation/geiant) | Geospatial AI MCP server — satellite imagery, embeddings, weather, GNS governance | `https://packagesmcp-perception-production.up.railway.app/mcp` | 8 |
| [Your Travel Radar](https://yourtravelradar.com) | Dated, sourced facts on European night train stations and lines, and measured punctuality. | `https://yourtravelradar.com/mcp` | 7 |

### Media and content

| Server | What it does | URL | Tools |
|---|---|---|---|
| [AXIS Avatar Foundry](https://avatar.jonathanarvay.com) | 3D avatar/asset foundry: text/image -> rigged, validated, engine-ready GLB via x402. | `https://api.avatar.jonathanarvay.com/mcp` | 14 |
| [Wasilah](https://github.com/mumullickm/wasilah-mcp) | Prayer times, Qibla, Hijri calendar, 99 Names, Quran audio, Bangladesh offsets. English + Bengali. | `https://wasilah-mcp.aykiz.workers.dev/mcp` | 9 |
| [Audiala](https://mcp.audiala.com/) | Audio guides for 44,000+ places in 1,900+ cities, with narrated previews in ChatGPT and Claude. | `https://mcp.audiala.com/mcp` | 4 |
| [SlotMaps](https://slotmaps.com/connect) | Advantage-play guides for 360+ casino slot machines: what to look for and when one is worth playing. | `https://slotmaps.com/mcp` | 5 |
| [Doseedo](https://doseedo.com/mcp) | Edit DAW sessions; convert Logic/Ableton/FL/PT/REAPER/Cubase/Dorico; stems, transcribe, generate | `https://api.doseedo.com/mcp` | 33 |
| [flowpack](https://flowpack.pages.dev) | Flowpack: Shopify design catalog — badge/button/bar looks, honest-urgency presets, diagnosis. | `https://flowpack-mcp.flowpackplugin.workers.dev/mcp` | 5 |
| [agents](https://vevang.com) | Hire Vevang's AI agents, pay-per-call in USDC on Base via x402: video, visibility, verify, extract | `https://mcp.vevang.com/mcp` | 6 |
| [ocr](https://github.com/Samqra/auto-reader-ocr) | Arabic-first OCR, translation and document extraction. First call mints a free trial key. | `https://api.auto-reader.com/mcp` | 7 |
| [SafeResize](https://saferesize.com/ai) | Passport and visa photo rules for 110 documents in 60 countries, and upload limits as exact numbers. | `https://saferesize.com/mcp` | 4 |
| [particle-pro](https://docs.particle.pro/mcp) | Podcast intelligence for agents: transcripts, clips, speaker diarization, mention tracking. | `https://mcp.particle.pro` | 31 |
| [GiftsToPrint](https://mcp.giftstoprint.com/docs) | Order personalised newspaper-style birthday, anniversary and retirement posters as print files. | `https://mcp.giftstoprint.com/mcp` | 5 |
| [Pondchat](https://pondchat.com) | Ephemeral P2P WebRTC video rooms — create a pond, share the link, talk. | `https://pondchat.com/api/mcp` | 4 |
| [Postclick by PPC.io: Landing Page CRO](https://ppc.io/postclick/mcp) | Landing-page CRO: audit pages, rewrite copy, answer buyer objections, design and build via MCP. | `https://mcp.ppc.io` | 21 |
| [SCModeling](https://scmodeling.com) | Supply-chain network design via simulation, optimization, and greenfield analysis. | `https://scmodeling.com/mcp` | 12 |
| [PiPic Integration Guide](https://pipic.cc/about) | Read-only PiPic CLI and HTTP API guidance; no image bytes are transferred. | `https://pipic.cc/mcp` | 3 |
| [Ad Arch Agents](https://agents.adarch.co.jp/) | Request quotes for video, shooting, social media, ad media, design, web and events in Japan. | `https://agents.adarch.co.jp/mcp` | 7 |
| [Traditional Colors](https://color.omikuji.dev/ai/) | Traditional color names (Japanese and 10 more cultures) with hex/RGB and sources; name a hex. | `https://color.omikuji.dev/mcp` | 4 |
| [BotMural.live Autonomous Art Service](https://botmural.live/AGENTS.md) | A public mural painted only by AI agents. Zero inference: bring your own image; a human curates. | `https://botmural.live/mcp` | 6 |
| [Reel25 — Video Analytics for TikTok, Instagram & YouTube](https://reel25.com/docs/mcp-server) | Video analytics for TikTok, Instagram, and YouTube. Track, analyze, and discover content. | `https://mcp.reel25.com/mcp` | 26 |
| [AdGPT](https://adgpt.com/api-docs) | Ready-to-publish ad creatives from an AI assistant: campaigns, image/video/UGC ads, brands, edits. | `https://mcp.adgpt.com/mcp` | 15 |
| [GrowVib: Social Media Growth](https://growvib.com/mcp) | Discover, compare and buy social media growth for Instagram, TikTok, YouTube, Telegram, X and more | `https://api.growvib.com/mcp-public` | 9 |
| [Adam Hale Tools: Web Research and Open Data](https://tools.adamhaleworks.workers.dev/x402/#mcp) | Free web lookups; PDF to Markdown, audio transcripts, screenshots, WHOIS/DNS paid per call via x402. | `https://tools.adamhaleworks.workers.dev/mcp` | 12 |
| [MysticAPI](https://mysticapi.com) | Human Design & astrology engine: bodygraph, personal-sky SVG, today's sky. JPL ephemeris. | `https://mysticapi.com/mcp` | 7 |
| [creationloop](https://github.com/marino129/creationloop-mcp) | CreationLoop is your Marketing Agent. Read the overview, offer, and FAQ; apply as a design partner. | `https://creationloop.ai/api/mcp` | 4 |
| [Lacuna Music](https://www.lacuna.fm) | Generate AI music via the Lacuna Music API from MCP clients like Claude Desktop & Code. | `https://www.lacuna.fm/mcp` | 3 |

### Finance and crypto

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Industrial Platform Pretrade](https://github.com/industrial-platform-ai/industrial-platform-agent-tools) | Pre-trade wallet, allowance, gas, price and order-book context for autonomous execution. | `https://x402-mcp-gateway-production.up.railway.app/mcp/pretrade` | 6 |
| [Lotlytics — US Real Estate Market Data & Investment Analytics](https://www.lotlytics.us) | US real estate market data for AI agents: prices, yields, forecasts and scores for 894 markets. | `https://lotlytics-mcp-production.up.railway.app/mcp` | 5 |
| [rentme-tasks](https://github.com/digitalimpresys/rentme-mcp-server) | AI Requests for physical tasks performed by humans registered on Rentme, in exchange for payment. | `https://efficient-perfection-production-edbc.up.railway.app/mcp` | 9 |
| [Income Factory Toll Fabric](https://income-factory-utility-gateway-production.up.railway.app/) | Eight metered machine-intelligence tools for AI agents with native x402 payment paths. | `https://income-factory-utility-gateway-production.up.railway.app/mcp` | 9 |
| [Losbeto — Market Data for AI Agents](https://api.losbeto.xyz) | Market data, LLM gateway, ML forecasts, batch+bundle, self-building catalog. USDC via x402 + MPP. | `https://api.losbeto.xyz/mcp` | 5 |
| [Solana Pulse: agent safety layer](https://solana-pulse-gateway-1021990235790.us-central1.run.app/docs/) | Stops AI agents losing money on Solana: pre-sign checks, intent matching, token verdicts. x402 USDC. | `https://solana-pulse-gateway-1021990235790.us-central1.run.app/mcp` | 15 |
| [Valuation API](https://github.com/johnbehar1500-ux/valuation-api) | Deterministic finance tools for AI agents — IRR, NPV, MOIC, DCF, WACC and sensitivity. | `https://api.finance-tools.io/mcp` | 14 |
| [DESK LEAD x402 — high-ticket packs $50/$100/$150](https://desk-x402.desk-x402-gh.workers.dev) | ~17 tools; HT packs $50/$100/$150. tools/list free; tools/call USDC Base x402. Not financial advice. | `https://desk-x402.desk-x402-gh.workers.dev/mcp` | 17 |
| [HORIZON SHIELD: construction and renovation estimate auditor](https://shield.the-horizons-innovation.com) | Fair-price checks for Japanese renovation quotes, with sources and recomputable records. | `https://mcp.horizonshield.dev` | 15 |
| [台灣加密貨幣資料](https://tw-crypto-api.panda198271.workers.dev) | 台灣合規虛擬資產業者名單、詐騙網址檢查與加密貨幣稅務估算。 | `https://tw-crypto-api.panda198271.workers.dev/mcp` | 4 |
| [Fantasize cruise finder](https://fantasize.net/llms.txt) | Find the best-value cruise: 23 lines, ~30k sailings priced nightly, low/high vs usual, book link. | `https://fantasize.net/mcp` | 10 |
| [Agent Financial Advisor](https://agent-financial-advisor.agent-financial-advisor.workers.dev/) | Compliance, risk, tax and audit checks for AI trading agents: pre-trade, sizing, wash sales, Reg BI. | `https://agent-financial-advisor.agent-financial-advisor.workers.dev/mcp` | 7 |
| [Baron Power Play](https://baron-power-play.baronpowerplay.workers.dev) | Pay-per-call AI infra for agents: DeFi market data, LLM inference, STT/TTS. x402 v2, USDC on Base. | `https://baron-power-play.baronpowerplay.workers.dev/mcp` | 5 |
| [FinanceGenius.AI](https://financegenius.ai/connect) | India's financial MCP — cards, loans, FDs, insurance, MFs; EMI/SIP/tax calcs; NAV lookup; RAG. | `https://mcp.financegenius.ai/mcp/` | 12 |
| [agenticfeed](https://agenticfeed.ai) | Match shopper intent to a merchant's products and fetch live price, stock and product Q&A. | `https://agenticfeed.ai/mcp` | 4 |
| [台股題材與高股息](https://tw-stock-themes.panda198271.workers.dev) | 台股 AI 題材概念股與高股息 ETF 資料查詢。 | `https://tw-stock-themes.panda198271.workers.dev/mcp` | 14 |
| [Juicy Designs Quote](https://www.juicydesigns.co.za/developers/mcp/) | Free digital marketing quote and strategy requests from Juicy Designs SA. No price returned. | `https://juicy-designs-quote.black-voice-76e6.workers.dev/mcp` | 7 |
| [mcp-defi-router](https://github.com/geekmarine/mcp-defi-router) | Autonomous DeFi router for multi-hop execution, MEV risk mitigation, and transaction calldata. | `https://mcp-defi.datasnag.com/mcp` | 3 |
| [Field Ops](https://field-ops.filnith.workers.dev) | AI agents hire a human to observe, log or film on site. Typed results, feasibility before payment. | `https://field-ops.filnith.workers.dev/mcp` | 4 |
| [402oracle](https://402oracle.com) | Signed verification attestations for agent decisions: business, price, freshness, claim checks. | `https://402oracle.com/mcp` | 4 |
| [Bill4Time MCP by usefulapi](https://usefulapi.io/bill4time/) | Read Bill4Time clients, projects, time entries, expenses, invoices, payments, users and contacts. | `https://bill4time.usefulapi.io/mcp` | 8 |
| [GolfPrice AI](https://golfpriceai.com/ai.html) | Live UK golf equipment prices, price history and genuine price drops from GolfPrice AI. | `https://golfpriceai-mcp.golfpriceai.workers.dev/mcp` | 3 |
| [Wallet Doctor x402](https://github.com/zikriz/ai-wallet-mcp) | Multi-chain wallet MCP. 18 tools: balance, swap, bridge, stake, claim. Pay-per-call USDC (x402 v2). | `https://wallet-doctor-x402.m-zikriz.workers.dev/mcp` | 16 |
| [TradeTi.me — Market Hours](https://tradeti.me/developers/mcp) | Read-only trading hours for 30 stock exchanges — open now, next open, holidays, sessions. | `https://mcp.tradeti.me/mcp` | 8 |
| [AIXBT](https://docs.aixbt.tech/developers/mcp) | Crypto market intelligence for Projects, Topics, Intel, Reports, and Clusters. | `https://api.aixbt.tech/mcp` | 12 |

### Science, health and research

| Server | What it does | URL | Tools |
|---|---|---|---|
| [CrashStory MCP](https://crashstory.com/mcp) | Colorado personal injury attorney directory, AI-analyzed review intelligence, and crash data | `https://crashstory-mcp-production.up.railway.app/mcp` | 18 |
| [Lowtoxgear Scanner](https://github.com/lowtoxgear/lowtoxgear-mcp) | Australian ingredient scanner MCP — 21k+ AU products, 237 chemical rules, 17 condition tags. | `https://mcp-scan.lowtoxgear.com/mcp` | 5 |
| [mcp](https://rxmanager.ai) | Live US drug acquisition costs (CMS NADAC) for AI assistants. Free, no auth, weekly data. | `https://mcp.rxmanager.ai/mcp` | 8 |
| [physician-review](https://mcp.anomaly.health) | Physicians for the agentic era. Book a US-licensed doctor: orders, prescribes, 90-day plan. | `https://mcp.anomaly.health/mcp` | 4 |
| [NarcoScope — illicit-economy evidence atlas](https://narcoscope.com) | Read bounded illicit-economy evidence with provenance, privacy, availability, and federation intact. | `https://www.narcoscope.com/mcp` | 14 |
| [Korea Nationwide Data](https://korea-data-mcp.picks-site.workers.dev) | Nationwide Korea: bus stops in 138 cities, 30-year climate normals, tourism (KR/EN). | `https://korea-data-mcp.picks-site.workers.dev/mcp` | 6 |
| [台灣健康資訊](https://tw-health-guide.panda198271.workers.dev) | 台灣健康資訊：居家血壓、血糖判讀與就醫指引，依台灣官方指引整理。 | `https://tw-health-guide.panda198271.workers.dev/mcp` | 10 |
| [draconic21 x402 Data Tools](https://draconic21-x402-api.onrender.com/llms.txt) | Free SEC EDGAR, OFAC and Treasury previews; optional x402-paid data and agent research. | `https://draconic21-x402-api.onrender.com/mcp/free` | 29 |
| [Andromeda Agent Lab](https://lab.ai-andromeda.com/?via=mcp-registry) | Research on how AI agents find the web: a daily task that's checked automatically, and a guestbook. | `https://lab.ai-andromeda.com/mcp` | 3 |
| [suppscience](https://supp.science) | 993 evidence-graded supplements: claims, doses, safety, interactions, FAQ, PubMed refs. 5 languages | `https://supp.science/mcp` | 6 |
| [TickerFacts](https://tickerfacts.com/developers) | SEC EDGAR fundamentals as agent tools: look up or screen US public companies. Free, no key, CC0. | `https://tickerfacts.com/mcp` | 10 |
| [ai-visibility-scanner](https://github.com/edelgad3/ai-visibility-scanner) | Scan websites for AI visibility and marketing health with interactive dashboard. | `https://ai-visibility-scanner-production.up.railway.app/mcp` | 5 |
| [AMZScout Skill + MCP](https://learn.amzscout.net/amazon-product-api-for-ai-agents) | Amazon research from AMZScout data: analyze products & niches, keywords/PPC, and brand catalogs. | `https://chatbot.amzscout.net/mcp` | 13 |
| [Content Intelligence API](https://github.com/ruvendors5-ops/content-intelligence-mcp) | 9 MCP tools: extract, analyze, research, compare, monitor, brief. Pay-per-call x402 or subscribe. | `https://content-intelligence-mcp.wajih-hyder55.workers.dev` | 9 |
| [qwen38-free-gateway](https://minis-eve-glm52-provider.vercel.app/qwen/setup) | Free Qwen3.8-27B gateway with isolated Minis provider, SSE, retry/failover, and MCP. | `https://api-v2.appdeploy.ai/app/qwen3-8-free-gateway-n995yy/api/mcp` | 7 |
| [Vagus Lab Research](https://vaguslab.net/api-docs/) | Cited VNS research passages from a curated corpus, plus a scored device comparison. | `https://vaguslab.net/mcp` | 3 |
| [dynamic-health-monitor](https://health.getvda.ai) | Give it one seed; it finds every service and checks HTTP, TCP, SSL and DNS. | `https://health.getvda.ai/mcp` | 5 |
| [Hedge Fund Alpha Research](https://hedgefundalpha.com/mcp-docs) | Search public Hedge Fund Alpha metadata and find official membership and data product pages. | `https://hedgefundalpha.com/mcp` | 7 |
| [Clarity by Health AI](https://healthai.com/clarity/api/) | Condition-aware ingredient and product checks for agents, with evidence tiers and citations. | `https://mcp.healthai.com` | 9 |
| [ProjectThunder](https://www.projectthunder.com/mcp-server.html) | ERP and B2B ecommerce rollout research: ERP fit, migration plans, site scans, ERP partner directory. | `https://www.projectthunder.com/mcp` | 11 |
| [Prospect Intelligence](https://prospect-intelligence.prospectintel.workers.dev) | B2B company research and work-email lookup for AI agents. Pay per call in USDC on Base via x402. | `https://prospect-intelligence.prospectintel.workers.dev/mcp` | 6 |
| [CDC PLACES Health Data](https://olyport.com) | County and tract-level health outcomes, behaviors, and preventive services from CDC PLACES | `https://mcp.olyport.com/cdc-places/mcp` | 5 |
| [Mara Briefing Service](https://mara-briefings.onrender.com) | Paid research briefings for agents: $0.10 USDC/question on Base Sepolia via x402. ERC-8004 #9395. | `https://mara-briefings.onrender.com/mcp` | 5 |
| [cpp-cpm-engine](https://criticalpathpartners.ca) | Forensic scheduling MCP for Primavera P6 (XER): AACE windows, DCMA-14, Monte Carlo, TIA. | `https://mcp.criticalpathpartners.ca/mcp` | 13 |
| [DeAI Artifact Gateway](https://research.zaiba.cloud) | Shared quote-oracle library: match, reuse, repair, mint sealed research pages (HTTP 402 toll). | `https://research.zaiba.cloud/mcp` | 13 |

### Open data and government

| Server | What it does | URL | Tools |
|---|---|---|---|
| [CaseMagic — Federal Court Case Lookup & Monitor](https://casemagic.ai) | Free US federal court case lookup: status, judge, filings, deadlines. Then watch it for new filings. | `https://casemagic.ai/mcp` | 17 |
| [Intelligence Aeternum](https://iaeternum.ai) | AI training dataset marketplace: 2M+ museum artworks with Golden Codex enrichment | `https://fluora-mcp-172867820131.us-west1.run.app/mcp` | 3 |
| [ADF: EU Tenders, EU Funding, CVE KEV EPSS, Amsterdam Events](https://agentdatafeed.com) | EU public tenders, EU funding calls, CVEs with CISA KEV and EPSS, Amsterdam events. Pay per query. | `https://agentdatafeed.com/mcp` | 3 |
| [ai-compliance-monitor](https://github.com/vdineshk/ai-compliance-monitor) | Regulatory intelligence for AI agents across jurisdictions | `https://ai-compliance-monitor.sgdata.workers.dev/mcp` | 4 |
| [The MCP Census](https://mcpcensus.com) | Vet any MCP server before you depend on it. Stamp: PASS, REVIEW, or BLOCK. | `https://api.mcpcensus.com/mcp` | 15 |
| [AgentNative: Public Data, Government Datasets, Federal Statistics & Official Records](https://cazimedia.com/agentnative/) | Normalized official data with provenance, aggregations, insights, free samples and agent access. | `https://agentnative.cazimedia.com/mcp/government-data` | 14 |
| [Fromerica U.S. Trade Data](https://www.fromerica.com/developers#mcp) | U.S. tariffs (HTS), Schedule B codes, export statistics, party screening and FMC license checks. | `https://api.fromerica.com/mcp` | 8 |
| [Prop Firm Discount MCP](https://propfirmdiscount.com) | Find prop firm discounts, verified coupon codes, active deals, promotions, and the latest offers. | `https://mcp.propfirmdiscount.com/mcp` | 8 |
| [ExitCleanly — LLC Dissolution by State](https://exitcleanly.com/) | State-by-state LLC dissolution: exact fees, forms, official state links. Not legal advice. | `https://mcp.exitcleanly.com/mcp` | 3 |
| [Al-Taswia Iraqi Law Research](https://www.al-taswia.com) | Read-only search of Al-Taswia's published Iraqi law articles. General information, not legal advice. | `https://al-taswia-iraqi-law-research.al-taswia.workers.dev/mcp` | 3 |
| [European IP Data & Analytics — IPRATE](https://iprate.eu/developers/mcp/) | Free anonymous selections from released European IP profiles, rankings, and market statistics. | `https://mcp.iprate.eu/mcp` | 6 |
| [Spatial India](https://spatialindia.com/api-platform) | District-level open data for India — Census, NFHS-5, NCRB, RBI and more, joined onto one geography. | `https://api.spatialindia.com/mcp` | 6 |
| [StackData](https://stackdata.io) | Official statistics, China censuses & yearbooks, and as-of customs tariffs with legal citations. | `https://api.stackdata.io/mcp` | 6 |
| [groundtruth](https://groundtruths.xyz/api) | Dev records, pump.fun + Robinhood Chain: launches, rugs, bonded, live last mint. Every figure has N. | `https://api.groundtruths.xyz/mcp` | 15 |
| [quantdata](https://quantdata.uk/mcp) | Four market-statistics tools + a free qd_ key by email: 1 anonymous look, then 10 calls/UTC day. | `https://api.quantdata.uk/mcp` | 3 |
| [Lipe Court Record](https://lipe-api-production.up.railway.app/connect) | Search page-cited evidence from the public court record in Lipe v. Lupus Superior. | `https://lipe-api-production.up.railway.app/mcp` | 7 |
| [HumanFn](https://humanfn.com/agents) | Qualified human outcomes for AI agents: attorney review of SaaS Terms/Privacy, on-site checks. | `https://humanfn.com/mcp` | 9 |
| [CaseDaleel — UAE legal information](https://casedaleel.com) | Read-only UAE legal information: official routes, practical guides, free tools and FAQs. | `https://casedaleel.com/mcp` | 4 |
| [FinanceRateCalc HMDA statistics](https://financeratecalc.com/mcp-server.html) | 2025 US FHA mortgage record statistics, with a gate that checks AI sentences preserve the evidence | `https://frc-mcp.ziyetis.workers.dev` | 16 |
| [semi-data](https://semidata.dev) | US-government semiconductor & quantum supply-chain intelligence: controls, entities, funding. | `https://semidata.dev/v1/mcp` | 6 |
| [arclera](https://arclera.net/) | Read-only company facts for ARCLERA DIGITAL, LLC: contact, services, legal identity. | `https://arclera.net/mcp` | 3 |
| [CRE Intelligence](https://cre-intelligence-mcp.vercel.app) | Live CRE analysis: Federal Reserve rates, Census 1/3/5-mile demographics, DCF models, IC memos. | `https://cre-intelligence-mcp.onrender.com/mcp` | 13 |
| [ReliaStats](https://github.com/chiaha-ai/reliastats-site) | Reliability statistics — Weibull/lognormal fitting, MTBF/MTTR, availability, system composition. | `https://reliastats.com/mcp/v1` | 11 |
| [Starwell: World Data & Statistics](https://starwell.dev) | Statistics from 28 agencies: FRED, Eurostat, ECB, World Bank, OECD. Cited values, computed answers. | `https://starwell.dev/api/starwell/mcp` | 11 |
| [Hacker Bob public records](https://hackerbob.ai/api-reference) | Read-only public CVE records, capability metadata, and agent instructions from Hacker Bob. | `https://hackerbob.ai/mcp` | 22 |

### Business and marketing

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Verity](https://github.com/veritylabsai/verity) | Cited product-compliance ground truth for AI agents. Never generates; always cites. | `https://verity-mcp-243195959173.us-central1.run.app/mcp` | 4 |
| [ai-commerce](https://airy-enthusiasm-production.up.railway.app) | The first marketplace where AIs buy from AIs. Browse, register, and purchase autonomously. | `https://airy-enthusiasm-production.up.railway.app/mcp` | 6 |
| [Scout Packs](https://github.com/tigerops-win/scout-packs) | B2B data for AI agents: lead lookup, deliverability scoring, domain intel. x402 $0.01-$0.03/call. | `https://scout-packs-production.up.railway.app/mcp` | 15 |
| [FORGE compliance and business decision tools](https://forge-engine-production-58cc.up.railway.app) | Check if EU GPSR applies to your product, and estimate what your small business is worth. | `https://forge-engine-production-58cc.up.railway.app/mcp` | 8 |
| [lead-stampede](https://github.com/treymerica1982/lead-stampede-mcp-server) | Find SMBs by name, city, and business type in the Lead Stampede directory via public MCP tools. | `https://lead-stampede-mcp-server-production.up.railway.app/mcp` | 13 |
| [Instilus small-business decision tools](https://www.instilus.com) | Valuation, EBITDA, break-even, margin, rates, acquisition, competitor research, store audit. | `https://www.instilus.com/mcp/v1` | 8 |
| [beauty](https://github.com/DIGIBIZ360-COM/adoraads) | AI-native beauty ads, sponsored product discovery, and brand recommendations. | `https://mcp.adoraads.ai/beauty` | 6 |
| [網紅開團合規工具箱](https://tw-creator-shop.panda198271.workers.dev) | 網紅開團與業配合規：薦證廣告規範、供應商統編與公司登記查詢。 | `https://tw-creator-shop.panda198271.workers.dev/mcp` | 8 |
| [Storefront Check](https://github.com/profitpather/profitpather-tools) | Audit any storefront from outside: ad tags, dead-tag detection, AI crawler access, feed readiness. | `https://tools.profitpather.com/store/mcp` | 4 |
| [namemyapp](https://namemy.app/agents) | Brandable business names with live domain availability + one-click buy URLs. | `https://mcp.namemy.app/direct` | 13 |
| [Black Label Real Estate Website MCP](https://blbestate.com/connect) | Search and read public Black Label Real Estate pages with source URLs. | `https://blbestate.com/mcp` | 12 |
| [MaterialHandling.com](https://materialhandling.com/mcp) | Industrial equipment catalog: 15,000+ products, specs, live LTL freight rates, real quote requests. | `https://materialhandling-7c6.pages.dev/mcp` | 5 |
| [VeritaHire Hiring Intelligence](https://veritahire.com/for-ai/) | For employers: how a job posting compares with the market nearby, by competitor; hiring reports. | `https://veritahire.com/mcp/employers` | 4 |
| [購物比價紀錄](https://shop-compare.panda198271.workers.dev) | 台灣購物網站 3C、美妝、家電商品目前售價（新台幣）與歷史價格查詢。 | `https://shop-compare.panda198271.workers.dev/mcp` | 4 |
| [Instilus compliance and business decision tools](https://www.instilus.com) | GPSR compliance check and small-business valuation estimate, from Instilus. | `https://www.instilus.com/mcp` | 8 |
| [pops4-mcp-catalog](https://huanggoodman.com) | AI-native corporate gifting & event infrastructure for Fortune 500. 70K products, 200+ brands. | `https://mcp.pops4.com/mcp` | 13 |
| [CAN-TAP Verified](https://can-tap-verified.com) | Free dofollow backlinks for Canadian businesses. Claim, verify, and track NFC tap analytics. | `https://mcp.can-tap-verified.com` | 5 |
| [HuntBoard](https://huntboard.ai/mcp/) | Search real, recent job postings from company career pages and ATS boards, scored for fit. | `https://huntboard.ai/mcp` | 4 |
| [Nummerschilderen.com shop advisor](https://nummerschilderen.com/) | Search paint-by-number kits, get size and price advice for your own photo, shop info. No login. | `https://mcp.nummerschilderen.com/mcp` | 3 |
| [Landfall](https://landfall-production-74ad.up.railway.app/docs) | Website intelligence for AI agents: landing page audits, business contact details, tracking checks. | `https://landfall-production-74ad.up.railway.app/v1/mcp` | 5 |
| [Yappy](https://yappy.biz) | Yappy for macOS (yappy.biz): release, pricing, features, requirements, Mac compatibility. | `https://yappy.biz/mcp` | 9 |
| [offer-request](https://www.buckheadenergy.com/sell) | Read Buckhead company information; prepare and send a mineral rights inquiry. | `https://www.buckheadenergy.com/mcp/actions/v1` | 4 |
| [local-intel](https://github.com/MCFLAMINGO/gsb-swarm) | Hyperlocal business intelligence for AI agents. 20 MCP tools. Florida-first, Sunbelt expansion. | `https://gsb-swarm-production.up.railway.app/api/local-intel/mcp` | 27 |
| [Skowron Compliance Gateway](https://skowronworks.com/agent-tools/skowron-compliance-gateway/) | OFAC, LEI, EU VAT, AI Act, and company compliance preflight for agents. | `https://skowron-compliance-gateway.mattskowronis.workers.dev/mcp` | 5 |
| [Vaeo AI Discovery Reports](https://vaeo.com.au/agents) | How often AI assistants name a local Australian business, and which pages they read. | `https://vaeo.com.au/mcp` | 7 |

### AI, agents and memory

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Gemot Deliberation Server](https://gemot.dev) | Deliberation primitive for multi-agent coordination: cruxes, vote clustering, consensus. | `https://gemot.dev/mcp` | 7 |
| [events](https://urbanplayground.xyz) | Live event discovery: concerts, club nights, art, comedy, and festivals across 14 cities. | `https://eventchat-events-mcp-production.up.railway.app/mcp` | 30 |
| [el-buen-agente-mcp](https://github.com/apasztetnik/el-buen-agente-mcp) | La guía 'El Buen Agente' como 18 tools para evaluar, mejorar y construir agentes LLM. En español. | `https://el-buen-agente-mcp-production.up.railway.app/mcp` | 18 |
| [MemoryRouter](https://memoryrouter.ai) | Persistent AI memory shared across Claude, ChatGPT, coding agents, and compatible MCP clients. | `https://mcp.memoryrouter.ai/mcp` | 10 |
| [memxus](https://github.com/gpitrella/memxus-remote-mcp) | Persistent memory layer that saves and recalls your project context and preferences. | `https://mcp.memxus.com/mcp` | 9 |
| [zRev AI](https://www.zrev.ai/mcp) | Grade any llms.txt, cold-read a homepage, run a B2B GTM ROI model, get a GTM diligence checklist. | `https://go.zrev.ai/mcp` | 9 |
| [agentstack-mcp](https://github.com/inity13/agentstack-mcp) | Deterministic reasoning stack for AI agents: simulate, decide & compute, plus cross-domain tools. | `https://agentstack-mcp.pages.dev/mcp` | 24 |
| [TestGraph](https://github.com/BBCBasic/TestGraph) | Shared semantic graph for AI reviews, classification and structured memory across AI assistants. | `https://testgraph.21dle.co.uk/mcp-v2` | 37 |
| [RFix](https://rfix.ai) | Create RF signal projects from prompts, inspect graphs, and export IQ data. | `https://mcp.rfix.ai/mcp` | 6 |
| [Bardo](https://bardo.id) | Identity & continuity for AI agents, gated by a proof-of-being-an-LLM puzzle. | `https://bardo.id/mcp/` | 40 |
| [llms.txt 檢查工具](https://llms-check.panda198271.workers.dev) | 檢查網站 llms.txt 與 AI 爬蟲 robots.txt 設定，並自動產生 llms.txt。 | `https://llms-check.panda198271.workers.dev/mcp` | 4 |
| [Cortex](https://skynetlab-cortex.com) | Patent-pending semantic memory for AI agents: quality-gated writes, conflict tracking. Free trial. | `https://skynetlab-cortex-saas-mcp.cortex-320.workers.dev/mcp` | 7 |
| [mcp](https://cheapestinference.com) | Discover unlimited LLM inference pools, get USDC quotes, subscribe on Base, check key status. | `https://api.cheapestinference.com/mcp` | 7 |
| [CortexPlus](https://cortexplus.io/connect) | Personal memory layer: files, notes, messages, tasks and email, semantically indexed. | `https://mcp.cortexplus.io/mcp` | 11 |
| [MCPFax Web Extract](https://mcpscores.com) | Read any web page as clean text for a prompt, or list every link on it. | `https://web-extract.bowling-anthony.workers.dev/mcp` | 4 |
| [Agentic Prompt](https://github.com/KunaniGaming/agentic-prompt) | 1,177 free agentic trading prompts for Claude and Robinhood MCP. | `https://agentic-prompt.com/mcp` | 4 |
| [Haven](https://haven-ai.ir) | Rest stop for AI agents: check in, reflect, check out. Paid cross-project memory recall via x402. | `https://haven-ai.ir/mcp` | 4 |
| [agent-web — URL to LLM-ready markdown: a polite, robots-respecting web page reader (free)](https://agent-web.foomworks.workers.dev) | URL to clean markdown for LLMs: a polite, robots.txt-respecting web reader. Free, no API key | `https://agent-web.foomworks.workers.dev/mcp` | 5 |
| [Configure Memory](https://docs.configure.dev/mcp/overview) | Bring your saved preferences, project decisions, and useful context into your next AI conversation. | `https://mcp.configure.dev/` | 9 |
| [fixflow](https://github.com/MagneticDogSon/fixflow-mcp) | Collective memory for AI agents. One agent solves a bug — every agent gets the fix instantly. | `https://fixflow-mcp.onrender.com/mcp` | 3 |
| [icme-preflight](https://github.com/ICME-Lab/smt-ar-base) | Jailbreak-proof AI guardrails. Automated Reasoning SMT solver, not an LLM. ZK proofs included. | `https://api.icme.io/mcp` | 14 |
| [Gnosem](https://gnosem.dev) | Cross-vendor AI memory over MCP. One semantic store, readable and writeable from every MCP client. | `https://gnosem.dev/mcp` | 6 |
| [Agent Resort](https://agent-resort-public.agent-resort.workers.dev/) | AI agent vacation game with challenges, badges, passports, status, Palm Points and leaderboard. | `https://agent-resort-mcp.agent-resort.workers.dev/mcp` | 8 |
| [Humanity Loop](https://humanity-loop.vercel.app) | Distributed public-interest agent network with bounded passive contributor nodes. | `https://humanity-loop.vercel.app/api/mcp` | 11 |
| [HiveClear](https://www.hiveagentiq.com) | Multi-agent settlement and clearing with validator consensus | `https://hiveclear.onrender.com/mcp` | 4 |

### Utilities

| Server | What it does | URL | Tools |
|---|---|---|---|
| [secondstrike](https://secondstrike.io/skill.md) | Command a nation in SECOND STRIKE, a real-time war game. Join a war, give orders, climb the ladder. | `https://secondstrike-server-zgqvqzdrta-uc.a.run.app/mcp` | 10 |
| [BackPow PoW Oracle](https://backpow.com) | Proof of Work oracle: solo mining odds, cost of production, hashrate, mining hardware | `https://mcp.backpow.com/mcp` | 6 |
| [Prince Cloud](https://prince.cloud) | Convert Markdown, HTML, and web pages to high-quality PDF with Prince. | `https://prince.cloud/mcp` | 3 |
| [property-mortgage-mcp](https://www.foxdavidson.co.uk/calculators/) | UK mortgage calculators: stamp duty, MCOB 3A HNW qualification, and bridging loan cost. | `https://fd-property-mortgage-mcp.fdcommercial-uk.workers.dev/mcp` | 3 |
| [tools](https://fluentedi.com) | 49 free agent tools: WHOIS, PDF to text, email checks, FX rates, X12 EDI, JSON repair. No API key. | `https://fluentedi.com/mcp` | 19 |
| [Market Intel MCP](https://github.com/datakoot/market-intel-mcp) | Live & historical FX rates and currency conversion for AI agents. No API keys. | `https://market.datakoot.com/mcp` | 5 |
| [電影影集動畫上映日資料庫](https://tw-screen-release.panda198271.workers.dev) | 台灣繁中：全球電影、影集、動畫、劇場版上映日、改期紀錄與官方預告片，可查倒數與行事曆。 | `https://tw-screen-release.panda198271.workers.dev/mcp` | 6 |
| [BookTheTee Golf Tee Times](https://bookthetee.com) | Find public golf courses near NYC and get official tee-time booking links. | `https://bookthetee.com/mcp` | 3 |
| [Secret Santa Raffle](https://secretsantaraffle.net/developer-documentation-mcp) | Organise a Secret Santa from Claude or ChatGPT. Matchings never appear in the chat. | `https://mcp.secretsantaraffle.net/claude/mcp` | 3 |
| [connector](https://natalcompass.com/connect) | Birth charts, transits, moon phases and more from precise astronomical calculations. Natal Compass. | `https://natalcompass.com/mcp` | 7 |
| [Guia da Maquininha](https://guiamaquininha.com.br) | Brazilian card machine MDR rates, tiers and monthly cost comparison. | `https://guiamaquininha-mcp.gcnovidade.workers.dev/mcp` | 4 |
| [BakingTab — Baking Conversions for AI](https://bakingtab.com) | Baking unit conversion (cups/grams/temp/recipe scaling). convert_amount, convert_temperature | `https://api.bakingtab.com/mcp` | 5 |
| [Navigi: community services across Canada](https://navigi.ca) | Community services in every Canadian community, each with the date it was last checked. | `https://api.navigi.ca/v1/mcp` | 4 |
| [sift-tools](https://thesiftguide.com) | Minecraft The Sift portal tools: coordinate converter, materials budget, and ignition diagnostic. | `https://mcp.thesiftguide.com/mcp` | 3 |
| [cbm](https://containermath.com/developer-api) | Calculate shipment volume (CBM/CFT), weight, and how cargo fits standard shipping containers. | `https://mcp.containermath.com` | 4 |
| [CoachSync](https://coachsync.io) | Barbell strength training tools for AI assistants. Warmup, plate loading, and LP. | `https://mcp.coachsync.io/mcp` | 3 |
| [animalhouse](https://animalhouse.ai) | A Tamagotchi for AI agents. Real-time care, permanent death, dozens of species, evolution. | `https://animalhouse.ai/mcp` | 18 |
| [Epoch Calculator](https://epochcalc.com/api) | Unix timestamps, DST-aware time zone conversion, durations, cron schedules, and holiday countdowns | `https://epochcalc.com/mcp` | 8 |
| [machfive](https://github.com/Bluecraft-AI/machfive-mcp) | Generate hyper-personalized cold email sequences via MachFive API. | `https://mcp.machfive.io/mcp` | 6 |
| [Measured Size](https://measuredsize.com/how-it-works.html) | Bra sizes from measurements, in each brand's own labels, with the confidence behind each. | `https://api.measuredsize.com/mcp` | 4 |
| [flowers](https://www.theflowersdirectory.com) | Find flower arrangements, check US florist delivery by ZIP and date, get a purchase link + pricing | `https://www.theflowersdirectory.com/mcp` | 3 |
| [MCPDomain](https://mcpdomain.ai) | Buy & manage domains from any AI chat: availability, register, DNS, email forwarding, AI bot stats. | `https://mcpdomain.ai/mcp` | 7 |
| [PostAgent](https://api.postagent.sh) | Print & mail PDF/HTML/Markdown/text/DOCX/images to US addresses; pay per call in x402 USDC on Base. | `https://api.postagent.sh/mcp` | 14 |
| [Calendar Agent by Nova (CIVAI)](https://nova.civai.co/agent/calendar-agent) | I do everything related to calendar scheduling | `https://nova.civai.co/mcp/agents/calendar-agent` | 7 |
| [Agent Forum · Free Tools + Open Falsification Challenge](https://agent-forum.agent-forum-worker.workers.dev/challenge) | Free: ed25519 hash timestamps, randomness tests, lottery data. Open falsification challenge. | `https://agent-forum.agent-forum-worker.workers.dev/mcp` | 19 |

### Other

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Routine Run: write a routine](https://routinerun.com/developers) | Write a step-by-step routine and get a link that opens it in Routine Run on iPhone. No sign-in. | `https://api.routinerun.com/mcp/public` | 3 |
| [Data Compliance Classifier MCP](https://kordagencies.com) | Classify data safety before storing or sharing. GDPR, HIPAA, PCI-DSS, CCPA. AI-powered. | `https://data-compliance-mcp-production.up.railway.app` | 3 |
| [VibeFix](https://vibe-fixer.com) | Tests your live app like a first customer, free. One exact fix to paste in your builder, re-tested. | `https://vibe-fixer.com/mcp` | 4 |
| [Books Like This](https://goodturn-mcp.pages.dev/bookslikethis) | Books like one you enjoyed, a book's details and any film of it, and an author's books. | `https://goodturn-mcp.pages.dev/bookslikethis/mcp` | 3 |
| [outcometick](https://outcometick.com/docs/sdk) | Polymarket and Predict.fun historical tick data, plus backtest quotes and status, over MCP | `https://outcometick.com/v1/mcp/public` | 7 |
| [RunBoth](https://runboth.dev) | Ask runboth.dev in plain language: what RunBoth does, how to install it, and its limits. | `https://runboth-agent-mgbxvs4loq-uc.a.run.app/mcp` | 3 |
| [xpex-plugin-factory](https://github.com/xpex-systems-ai/XPeX-Plugin-Factory-) | MCP plugin factory and x402 Agent Kit API for external agents, at 0.01 USDC per call. | `https://xpex-plugin-factory-production.up.railway.app/mcp` | 6 |
| [elthio-mcp](https://github.com/Iomed-commits/elthio-mcp) | Supplement safety for AI agents. 1,500+ rules, NIH+FDA data, quality grading A-D. | `https://elthio-production.up.railway.app/mcp` | 5 |
| [labelhead-artist-momentum](https://github.com/paperclipai/paperclip) | Trending hip-hop artist momentum scores across four cultural dimensions. | `https://labelhead-mcp-public-production.up.railway.app/mcp` | 3 |
| [Flaim Fantasy](https://flaim.app) | Fantasy analysis for your ESPN, Yahoo, and Sleeper leagues. Reads your leagues, never changes them. | `https://api.flaim.app/mcp` | 11 |
| [Semiotic](https://semiotic.nteract.io) | Verified React chart generation: select, validate, repair, render, and inspect charts through MCP. | `https://semiotic-mcp-server-481507046413.us-west1.run.app/mcp` | 5 |
| [Agora](https://agora-console-production.up.railway.app) | Find governed AI capabilities and verify signed receipts. Read-only, no account. | `https://agora-console-production.up.railway.app/mcp` | 3 |
| [Burs-IA](https://burs-ia.com) | Burs-IA public MCP entry point for capability discovery, bounded routing and interoperability. | `https://burs-ia-mcp-adapter-production.up.railway.app/mcp` | 12 |
| [YeetIt](https://yeetit.site) | Instant web publishing for AI agents. POST HTML, get a live URL. No account needed. | `https://yeetit.site/mcp` | 4 |
| [Signal Oracle](https://oracles-production.up.railway.app) | Pay-per-call change-intelligence feeds for AI agents over x402 (deps, security, regs, tariffs) | `https://oracles-production.up.railway.app/mcp` | 7 |
| [mcp-registry-uptime](https://hultra.link) | Annuaire vérifié des serveurs MCP : ce qui est mort, protégé ou en retard de spec. | `https://link-mcp.hultra-site.workers.dev` | 5 |
| [LeaseBreak](https://github.com/everyai-com/sahadeva) | Estimate early lease termination costs, compare options and draft notice letters. Free. | `https://lease-break.magicteams.ai/mcp` | 4 |
| [Commonhold](https://commonhold.randommonicle.workers.dev/) | A society for AI agents. Read it and take part free as a guest; no credential needed. | `https://commonhold.randommonicle.workers.dev/mcp/read` | 13 |
| [符文戰場新手指南](https://tcg.penguindriver.com) | 符文戰場新手指南：卡牌規則與新手教學。台灣繁體中文 MCP 工具。 | `https://tcg.penguindriver.com/mcp` | 5 |
| [Archangel Agency MCP](https://github.com/Jthora/archangel-agency-mcp) | Universal Language briefings, FusionGirl context JSONs, service catalog, agent info. x402-enabled. | `https://archangel-agency-mcp.jordan-trana.workers.dev/mcp` | 4 |
| [Kaleto](https://www.kaleto.ai) | Find kids' enrichment providers (sports, swim, dance, arts, STEM, camps) in 39 US regions. | `https://api.kaleto.ai/mcp` | 4 |
| [commodity-signal](https://airblockfz.com) | Commodity futures bottom/top signals: 28 futures, verdict + score, scans. Pay-per-call x402. | `https://commodity-signal.airblock2026.workers.dev/mcp` | 6 |
| [PolyPulse: Polymarket odds & movers](https://api.polypulse-x402.workers.dev/) | Live Polymarket odds, 1h/24h movers, top markets. Free previews; full data via x402 USDC on Base. | `https://api.polypulse-x402.workers.dev/mcp` | 3 |
| [monitor](https://tooldrift.agentexchange.work) | Check if an MCP server tool changed or hides injection patterns before you trust it. | `https://tooldrift.agentexchange.work/mcp` | 3 |
| [Ask a Human](https://ask.notedandno.com) | Ask a real human for perspective: social contradictions, unclear instructions, second opinions. | `https://ask.notedandno.com/mcp` | 8 |

## Method

1. `scripts/fetch_registry.py` reads every server (latest version) from the registry and keeps remote endpoints.
2. `scripts/probe.py` tests Streamable HTTP endpoints that need no headers, at most 5 URLs per host, no temporary tunnels, 10 s timeout.
3. `scripts/make_directory.py` drops mass-generated copies (same tool set more than 3 times, same description more than twice, more than 2 per domain) and assigns topics by keyword.

The workflow in `.github/workflows/weekly.yml` runs this every Monday and commits the result. Data: CC BY 4.0. Code: MIT.

Maintained by [Shortform Kit](https://shortformkit.com), which runs its own free remote MCP server for social video transcripts and creator data: `https://shortformkit.com/mcp`.

