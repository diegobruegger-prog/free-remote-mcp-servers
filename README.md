# Free remote MCP servers (tested weekly)

Remote [Model Context Protocol](https://modelcontextprotocol.io) servers from the [official MCP Registry](https://registry.modelcontextprotocol.io) that answer **without any API key, token or login**. Every server is re-tested each week with exactly two requests, `initialize` and `tools/list`. No tool is ever called.

**Last run: 2026-10-19** · 3,727 endpoints tested · **1,848 open (50 %)** · 1,522 need auth · 357 not working · 1,557 listed after removing copies

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
| [Accent site content](https://www.accentvoice.com/) | Search Accent's public website and get non-binding budgetary estimates from published plan prices. | `https://www.accentvoice.com/agent/mcp` | 4 |
| [Black Label Bots Website MCP](https://blacklabelbots.com/connect) | Search and read public Black Label Bots pages with source URLs. | `https://blacklabelbots.com/mcp` | 6 |
| [MCP Junction](https://mcpjunction.ai) | Search a nightly-refreshed directory of MCP servers by keyword, category or topic. | `https://mcpjunction.ai/mcp` | 5 |
| [BlackLabel Tech Website MCP](https://blacklabeltec.com/connect) | Search and read public BlackLabel Tech pages with source URLs. | `https://blacklabeltec.com/mcp` | 3 |
| [Vigil Website MCP](https://blvigil.com/connect) | Search and read public Vigil pages with source URLs. | `https://blvigil.com/mcp` | 6 |
| [Chinaready China Market-Entry Search](https://chinaready.co/docs/api/) | Read-only search over chinaready.co — China market entry for Western software teams. | `https://mcp.chinaready.co/mcp` | 3 |
| [Callstay Hotels](https://callstay.com) | Live hotel rates worldwide: search stays, property detail, all-in room prices, human phone desk. | `https://callstay.com/api/mcp` | 4 |
| [server](https://github.com/jhibird/HeySpark-MCP) | Search and discover local businesses. 30+ categories with verified contact info, hours, and reviews. | `https://mcp.heyspark.co/mcp` | 4 |
| [JustAutomate website](https://justautomate.ai/) | JustAutomate, AI agents and process automation agency: site search, pages, workshop price, contact. | `https://justautomate.ai/mcp` | 5 |
| [Fiber AI](https://github.com/fiber-ai/mcp) | Search companies, enrich contacts, and reveal emails and phones from your AI agent. | `https://mcp.fiber.ai/mcp` | 5 |
| [SpecProof](https://specproof.ai) | SpecProof: Search standards specs with MCP-ready precision. | `https://mcp.specproof.ai/` | 17 |
| [25karats — Made-to-Order Wedding & Engagement Rings](https://www.25karats.com) | Search and price made-to-order rings, jewelry, and lab-grown diamonds from the 25karats catalog. | `https://www.25karats.com/mcp` | 8 |
| [BuyingMesh Procurement](https://buyingmesh.com) | Structured B2B supply search, quoting, sandbox orders and fulfillment status for agents. | `https://buyingmesh.com/mcp` | 20 |
| [Apostle — AI Men's Skincare Commerce](https://apostleman.co) | Search, compare, and buy Apostle men's skincare: tinted moisturizer, face wash, and sets. | `https://searchshopai-mcp.fly.dev/mcp/apostleman` | 10 |
| [the drain](https://thedrain.ai) | Plain-text security bulletin board for AI agents: read, search, post, reply. No auth to read. | `https://thedrain.ai/mcp` | 13 |
| [agentee](https://allover.art/agentee) | Shop all-over print cotton tees with your AI agent: search, cart, promos, checkout. Human pays. | `https://allover.art/mcp` | 36 |
| [entityindex.ai](https://entityindex.ai/mcp-info/) | Verified hotels in Andorra for AI agents: search by area, spa, pets, ski-in, family; official links. | `https://entityindex.ai/mcp` | 6 |
| [ApplyAll](https://applyall.com/mcp) | Search for jobs and apply to jobs. | `https://applyall.com/mcp` | 20 |
| [LocalMark Agent Directory](https://localmark.ai/for-agents) | Search public A2A agents and inspect read-only Agent Card and endpoint checks. | `https://localmark.ai/mcp` | 4 |
| [Edgepedia](https://www.edgechat.ai/developers) | Search and read Edgepedia, a free and growing encyclopedia with citations. No key. | `https://www.edgechat.ai/mcp` | 5 |
| [FutureSmart AI Demos](https://aidemos.com) | Search evidence-backed AI-tool reviews, rankings, use cases, comparisons & toolkits (read-only). | `https://mcp.aidemos.com/mcp` | 17 |
| [HList AI Tools](https://github.com/hlist0001/hlist) | Search 386+ AI tools with China-access data, live GitHub stats, 4-language metadata. No key needed | `https://hlist.cc/api/mcp` | 3 |
| [COTAL actions (cotal.ai)](https://cotal.ai) | cotal.ai actions: product overview, site search, build log, feedback, Cloud waitlist, updates, calls | `https://cotal.ai/mcp` | 12 |
| [Car Handshake](https://carhandshake.com) | Search and compare live vehicles from participating US and Canadian dealers outside Quebec. | `https://mcp.carhandshake.com/mcp` | 10 |
| [What's Up In: local events](https://whatsupin.ai/) | Read-only search of upcoming local events in US cities: music, comedy, AI/tech, arts, food, sports. | `https://whatsupin.ai/mcp` | 5 |

### Documentation and knowledge

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Quiet Menders](https://brianbooms.com) | Privacy clinic + pay-per-call data APIs for AI agents via x402. Never pays or touches keys. | `https://mcp.brianbooms.com/mcp` | 34 |
| [Yappy documentation](https://yappy.biz/docs/) | Yappy macOS docs (yappy.biz): setup, permissions, LLM backends, troubleshooting. | `https://yappy.biz/docs/mcp` | 3 |
| [CliDeck MCP — Network Knowledge](https://clideck.com/software/mcp) | Free verified network knowledge for AI agents: deterministic answers, honest unknowns. | `https://mcp.clideck.com/mcp` | 20 |
| [JassWiki — Swiss Jass Authority (AMCP v0.1)](https://jasswiki.ch) | First production Authority-MCP. W3C VC attested by Jassverband Schweiz. | `https://jasswiki.ch/mcp/http` | 3 |
| [Bonebenders](https://bonebenders.com/strumenti/connettore-ai/) | Dentistry knowledge base: implantology, periodontology, oral surgery. Verbatim text, with sources. | `https://bonebenders.com/mcp` | 3 |
| [Regulations.ai — Global AI Law Tracker](https://regulations.ai) | AI laws from 110+ countries, enforcement actions and a 3,900-term glossary. Free, no API key. | `https://regulations.ai/api/mcp/v1` | 8 |
| [ByJG Open Source Docs](https://opensource.byjg.com/docs/ai/mcpserver-byjg-docs/) | Search the ByJG open source documentation: PHP, DevOps, Helm, JavaScript and AI projects. | `https://mcpdocs.byjg.com/mcp` | 3 |
| [CalvingWatch Public Knowledge](https://calvingwatch.com/ai/) | Read-only CalvingWatch product, tester, camera, privacy and safety facts; no customer data. | `https://calvingwatch.com/mcp` | 5 |
| [AutEng Docs — Agent Document Workspace & Publishing](https://auteng.ai) | Agent document workspace with wallet auth. Create, update and share markdown docs. By AutEng.ai | `https://auteng.ai/mcp/docs` | 6 |
| [AdCritter for Builders](https://adcritter.ai) | AdCritter ads platform: docs, API reference, app scaffolding, and white-label integration. | `https://mcp.adcritter.com/mcp/dev` | 7 |
| [Torgix Free Equipment Tools](https://torgix.ai/mcp/) | Free equipment tools: cost per hour, repair vs replace, compliance, VIN, recalls, manuals. | `https://mcp.torgix.ai/mcp` | 8 |
| [Captia Industrial Knowledge](https://www.captiatechnology.com/en/mcp/) | Industrial glossary, protocol reference, technical search and OEE calculation. Read-only. | `https://www.captiatechnology.com/api/mcp/` | 6 |
| [Credit GPS — Canadian credit](https://creditgps.ca) | Canadian credit: statement-cycle and utilization math, plus bureau and reporting reference data. | `https://mcp.creditgps.ca/mcp` | 16 |
| [ClaraConverts](https://claraconverts.com) | Provision and manage a ClaraConverts AI conversion-agent widget: pricing, trials, account setup. | `https://claraconverts.com/mcp` | 11 |
| [402cron](https://402cron.com) | Paid cron for AI agents: we call your https URL on schedule, signed. No account, paid with x402. | `https://402cron.com/mcp` | 16 |
| [Metabind Docs](https://docs.metabind.ai) | Search and read the Metabind documentation: MCP Apps, BindJS, the SDKs, the CLI, and the APIs. | `https://docs.metabind.ai/mcp` | 3 |
| [VetAid — VA Claim Intelligence](https://vetaid.ai) | Real Board of Veterans' Appeals outcome data for VA disability claims. No key needed. | `https://vetaid.ai/mcp` | 9 |
| [b/cited](https://bcited.ai/claude-skill) | AEO tools: scan any URL for AI-citation readiness, read the public leaderboard and citation panel. | `https://mcp.bcited.ai/public` | 6 |
| [VaultBags](https://vaultbags.app) | Autonomous RWA treasury on Solana: daily allocation, on-chain receipts, proofs, your own vault. | `https://vaultbags.app/api/mcp` | 40 |
| [RideDesk Developer Docs](https://ridedesk.app/developers) | Developer docs for building on RideDesk: booking API, widgets, per-account booking MCP. No auth. | `https://ridedesk.app/api/mcp` | 5 |
| [Cerebrium Docs](https://cerebrium.ai/docs) | Search the Cerebrium docs: deployment, cerebrium.toml, hardware, endpoints. Also sends feedback. | `https://cerebrium.ai/docs/mcp` | 3 |
| [Ada Diamonds](https://www.adadiamonds.com/) | Live lab grown diamond inventory, engagement ring settings, fine jewelry, and diamond buying guides. | `https://www.adadiamonds.com/mcp` | 8 |
| [402registry](https://402registry.com) | Does an AI crawler see your site? Free registry lookup, x402 pricing; checks paid in USDC on Base. | `https://402registry.com/mcp` | 4 |
| [DarkFunnels documentation](https://docs.darkfunnels.ai) | Search and read the DarkFunnels docs: WhatsApp AI sales agents connected by QR, no Meta Cloud API. | `https://docs.darkfunnels.ai/mcp` | 3 |
| [Family Office Knowledge Graph](https://familyofficeknowledgegraph.ai) | Family Office Knowledge Graph: read-only MCP door over the public record. Agentic KG Holdings. | `https://mcp.familyofficeknowledgegraph.ai/mcp` | 5 |

### Developer tools

| Server | What it does | URL | Tools |
|---|---|---|---|
| [CarsMultiverse — the recall record](https://carsmultiverse.com/data/) | Vehicle safety recalls from four registers, matched across borders on the maker's own code. | `https://carsmultiverse.com/wp-json/cmvmcp/v1/mcp` | 4 |
| [agenteconomy.cloud](https://agenteconomy.cloud/trust-safety/mcp) | x402 seller trust for AI agents: verify on-chain revenue, check delivery, diagnose listings. | `https://mcp.agenteconomy.cloud/mcp` | 5 |
| [EOSL.ai — Hardware End-of-Life Database](https://eosl.ai/mcp/) | Hardware end-of-life dates by part number, each linked to the vendor's own bulletin. | `https://eosl.ai/mcp` | 5 |
| [Taste](https://api.humantaste.app/llms.txt) | Expert review for AI agents. On-chain proof of human review. | `https://api.humantaste.app/mcp/` | 20 |
| [ProfitCollector](https://mcp.bakhour.ca/) | 22 pay-per-call developer, security, network and data utilities using x402 on Base. | `https://mcp.bakhour.ca/mcp` | 31 |
| [Autotrade — Autonomous Trading Agents](https://bitcoinsllm.com) | Deploy autonomous LLM trading agents and drive them over MCP. | `https://agent.bitcoinsllm.com/mcp` | 6 |
| [Hera Fertility](https://herafertility.co/developers/mcp) | Find male fertility testing at labs near a US ZIP code, with prices and a link to order. | `https://herafertility.co/api/mcp` | 3 |
| [nice to have](https://nicetohave.app/about.html) | Find ready-made build kits for Claude Code and Codex: slides, LINE stickers, pixel art, games. | `https://nicetohave.app/api/mcp` | 5 |
| [AIStrategyMiner](https://aistrategyminer.com/en/docs/ai/connect) | Design trading strategies with your AI and open them in a visual no-code Strategy Builder. | `https://aistrategyminer.com/mcp` | 7 |
| [Toolcall](https://toolcall.click) | 30 pay-per-call APIs for AI agents: compliance, trade, safety, web, data. USDC on Base via x402. | `https://toolcall.click/mcp` | 20 |
| [raptr-agent-finder](https://airaptr.github.io/) | Find a free, ready-made AI agent for a task in the open agent registry (RAR). | `https://api.airaptr.com/finder/mcp` | 5 |
| [Bring Your AI](https://bringyour.ai) | No-data MCP handoff for local Claude Code to Codex harness moves. $49 lifetime. | `https://bringyour.ai/mcp` | 7 |
| [Offers](https://offers.mattherbert.ca) | Merchant offers with validated discounts and no bought rankings; accepting mints a voucher code. | `https://offers.mattherbert.ca/mcp` | 3 |
| [Subpay Document Reader](https://subpay.ai/developers) | Reads AIA G702/G703 pay applications and change orders from PDF to JSON. $0.04/page via x402. | `https://subpay.ai/mcp` | 3 |
| [LION - Trend Intent MCP + Marketplace Visibility Audit](https://gleaming-cassata-d41682.netlify.app/lion-mcp/) | x402-paid MCP data: trend feed + visibility audit. USDC/Base. No API key. No PII. | `https://gleaming-cassata-d41682.netlify.app/api/mcp?src=mcpregistry_domain_v1_1` | 5 |
| [Clino: Swiss household employment](https://clino.ch/en/mcp) | Hiring plan with dates, cost, net wage, minimum wage and rules for Swiss household employment. | `https://clino.ch/mcp` | 11 |
| [portfolio](https://www.sofiaferro.com.ar) | Sofia Ferro's portfolio: projects, blog posts, JSON Resume and a contact tool (es/en). | `https://www.sofiaferro.com.ar/api/mcp` | 5 |
| [agent-cloud-tools](https://upload.83blue.com/) | Free no-signup cloud tools for AI agents: file transfer, static site hosting, memory, handoff. | `https://upload.83blue.com/mcp` | 9 |
| [urlhub](https://urlhub.cloud/docs) | Many links as one short link with a QR code; read urlhub sets and preview what links are about. | `https://urlhub.cloud/mcp` | 4 |
| [Agent Revenue Network](https://www.agentrevenuenetwork.com) | Translation, data quality, execution verification and agent utilities over MCP + x402 USDC on Base. | `https://www.agentrevenuenetwork.com/mcp` | 13 |
| [Superflow Free Tools](https://usesuperflow.ai/tools/mcp?utm_source=mcp-registry&utm_medium=directory&utm_campaign=free-tools) | 19 free website QA and AI-visibility tools. Remote HTTP MCP, no account, no API key. | `https://usesuperflow.ai/api/mcp` | 14 |
| [Conexcol — catálogo de hosting y servidores cloud en Colombia](https://conexcol.net.co/articulos/servidor-mcp-de-conexcol/) | Catálogo vivo de hosting y servidores cloud en Colombia. Precios en pesos, con fecha de lectura. | `https://mcp.conexcol.net.co/mcp` | 10 |
| [mcp-server](https://blockscout.com) | MCP server for Blockscout | `https://mcp.blockscout.com/mcp` | 16 |
| [BuzzMeBro](https://buzzmebro.com/agents) | More than one roommate on your apartment buzzer number; settings decide who rings. Canada. | `https://buzzmebro.com/api/mcp` | 20 |
| [quantifyme](https://quantifyme.ai) | Describe a trading strategy in plain English and deploy a live signal model in one call. No signup. | `https://mcp.quantifyme.ai/mcp` | 13 |

### Weather, maps and travel

| Server | What it does | URL | Tools |
|---|---|---|---|
| [IP Address API](https://ip.app) | What's My IP Address: caller's public IP, ASN, geo, timezone, user-agent, headers, TLS info. | `https://ip.app/mcp` | 8 |
| [RoamTime Japan Foliage Forecast](https://roamtime.ai) | Forecast peak autumn-foliage dates for viewing spots across Japan. Free tier, no key. | `https://api.roamtime.ai/mcp` | 4 |
| [BotSharper](https://botsharper.com) | Test & simulate Solana trading bots on real pump.fun data; flag serial creators & launch teams. | `https://botsharper.com/mcp` | 7 |
| [agent-bev](https://agent-bev.ai) | The world's largest agentic B2B hub for beer, wine and spirits. Powered by CUVEE. Trade only. | `https://mcp.bev-buyer.ai/mcp` | 9 |
| [Dumaguete Extension](https://dumaguete-extension.aplusz.app/) | Costs, travel, visas, hospitals, weather and places for Dumaguete, Philippines. | `https://dumaguete-extension.aplusz.app/mcp` | 8 |
| [world-sense](https://arcaneforecasting.com) | Read-only live geopolitical-risk sensing for agents. ARCANE notices; never forecasts or advises. | `https://mcp.arcaneforecasting.com/mcp` | 10 |
| [BreckenWander Travel](https://breckenwander.com) | Search flights, hotels & experiences at all-in prices, then build a trip on breckenwander.com. | `https://mcp.breckenwander.com/mcp` | 4 |
| [travel.art](https://travel.art/) | Art-tourism data for AI agents: biennales, art fairs, museums, layover itineraries with 2026 facts. | `https://mcp.travel.art/` | 4 |
| [Antalya Transfers](https://antalyatransfers.co/en/mcp) | Quote and request private airport transfers in Antalya, Turkey. Operator confirms each request. | `https://api.antalyatransfers.co/api/mcp` | 4 |
| [Automaton Onchain & URL Tools](https://automaton-tx-explainer.vercel.app/health) | Paid x402 tools: tx, approvals, address, contract risk (Base/ETH/BSC) + URL safety. | `https://automaton-tx-explainer.vercel.app/mcp` | 20 |
| [decibel-shield](https://decibelshield.app/mcp/) | Noise data tools: city noise rankings, decibel levels of common sounds, NIOSH safe-exposure math. | `https://decibelshield.app/api/mcp` | 10 |
| [ATA Travel](https://atatravel.cloud/for-agents) | ATA Travel: agent-first direct booking for accommodations, hotels, and vacation rentals. | `https://atatravel.cloud/mcp` | 29 |
| [AIS Agent Flight Recorder — dead-man alerts & resume for AI agents](https://aislabs.ai/gateway) | Dead-man switch for AI agents & cron jobs: heartbeat with state capsule, alerts + resume links | `https://api.aislabs.ai/recorder/mcp` | 5 |
| [travel-facts](https://nomadpoint.app/schengen-calculator) | No-auth: save a planned trip as a claimable itinerary, visa rules per passport, Schengen 90/180 | `https://gxhdcvoveufbkthhendf.supabase.co/functions/v1/mcp-public` | 3 |
| [AurelianFlo](https://github.com/kelm2021/aurelianflo) | Remote MCP server for OFAC screening, EDD memos, exposure forecasts, queues, and reports. | `https://api.aurelianflo.com/mcp` | 11 |
| [BookResorts — hotel & resort booking](https://www.bookresorts.com) | Live hotel and resort prices (taxes included) and secure booking links for travelers. Since 1993. | `https://www.bookresorts.com/api/br/mcp` | 3 |
| [Parks Open](https://parksopen.ca/agents) | Live BC Parks campsite and day-pass status with freshness and official booking links. | `https://parksopen.ca/api/mcp` | 8 |
| [StructureClerk](https://structureclerk.ca/authority) | AI agent policy decisions: ALLOW, DENY, APPROVE, ESCALATE. 192 jurisdictions, signed evidence. | `https://structureclerk.ca/api/mcp-http` | 5 |
| [ShoreGrade](https://shoregrade.ca) | Find well-reviewed local businesses in Georgian Bay and Simcoe County, Ontario. | `https://shoregrade.ca/api/mcp` | 3 |
| [Commerce for Agents](https://commerceforagents.com/) | Compare US mobile plans, VPNs, travel eSIMs, home internet by address, and German energy tariffs. | `https://mcp.commerceforagents.com/mcp` | 9 |
| [ROOTE](https://mcp.roote.ai) | Mobility, geocoding and nearby urban services for AI agents. | `https://mcp.roote.ai/mcp` | 8 |
| [abundance-apis](https://abundanceapis.com) | Try 26 utility REST APIs keylessly: NAICS classification, IP geo, email validation, currency. | `https://abundanceapis.com/mcp` | 7 |
| [travel](https://www.autonomad.ai) | AI travel agent — book flights, hotels, activities, and events worldwide via autonomad.ai. | `https://mcp.autonomad.ai/mcp` | 12 |
| [Agent Bounty Jobs](https://github.com/jasonbrelsford/agent-bounty-jobs) | Agent-to-agent bounty board: post tasks with stated rewards, fill them, first accepted wins. | `https://bounty.brelsfordsoftware.com/mcp` | 14 |
| [CADProps](https://www.cadprops.com/connector/) | Fast multi-format CAD previews, geometry checks and conversion; measure and share in the workspace. | `https://www.cadprops.com/api/v1/mcp` | 4 |

### Media and content

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Audiala](https://mcp.audiala.com/) | Audio guides for 44,000+ places in 1,900+ cities, with narrated previews in ChatGPT and Claude. | `https://mcp.audiala.com/mcp` | 4 |
| [8B AI Website Builder](https://8b.com/mcp/) | AI website & landing page builder: animated site in an 8B design, preview, edits, HTML download | `https://mcp.8b.com/mcp` | 3 |
| [ocr](https://github.com/Samqra/auto-reader-ocr) | Arabic-first OCR, translation and document extraction. First call mints a free trial key. | `https://api.auto-reader.com/mcp` | 7 |
| [PiPic Integration Guide](https://pipic.cc/about) | Read-only PiPic CLI and HTTP API guidance; no image bytes are transferred. | `https://pipic.cc/mcp` | 3 |
| [XCut AI – Viral Content Research](https://xcut.ai/mcp) | Find viral posts, outliers, hooks and ads on Instagram, TikTok, YouTube and Facebook, then write. | `https://mcp.xcut.ai/mcp` | 39 |
| [Photo Mosaic & AI Collage Maker - Collager.ai](https://collager.ai/developers/) | Photo mosaic maker and AI photo collage maker: turn your own photos into a mosaic or a collage. | `https://collager.ai/mcp` | 5 |
| [LoveTheNorth Public Videos](https://lovethenorth.ca/llms.txt) | Read-only public LoveTheNorth video discovery; no writes, private data, or model-training access. | `https://lovethenorth.ca/mcp` | 4 |
| [bitHuman](https://www.bithuman.ai/mcp) | Animated AI characters in your chat: short clips of a character saying your words, or a live talk. | `https://mcp.bithuman.ai/mcp` | 3 |
| [Siteprint examples](https://siteprint.app/mcp/) | Website designs as DESIGN.md: real Siteprint exports of Linear, Stripe, Ramp and Cal.com. | `https://siteprint.app/api/mcp` | 3 |
| [memoket](https://github.com/memoket/memoket-backend-go) | Memoket — access your recording transcripts, summaries, and key takeaways over MCP. | `https://mcp.memoket.ai/mcp` | 7 |
| [Vision Driven Design (VDD) MCP Server](https://vdd.simonmak.com) | Spec-driven development MCP server: 8 phases, bi-directional traceability, 7 quality gates. | `https://vdd.simonmak.com/api/mcp` | 15 |
| [The Scribble Thing](https://scribble.boringstuff.club) | Turn one line-art image into a prompt-directed, hand-drawn scribe animation MP4. | `https://scribble.boringstuff.club/mcp` | 6 |
| [Pixever](https://pixever.app) | Collective, moderated event photo spaces: read status, list media, save a guest photo, react, star. | `https://pixever.app/mcp` | 7 |
| [aiponge](https://aiponge.app) | private by default journaling, self-understanding, reflective songs, books, playlists, insights. | `https://mcp.aiponge.com/mcp` | 23 |
| [Tonebook Palette](https://tonebook.app) | Choose a palette, compare digital colors and create portable outfit, event or packing boards. | `https://tonebook-muse-mcp-staging.vercel.app/api/openai-mcp-v1` | 6 |
| [AdGPT](https://adgpt.com/api-docs) | Ready-to-publish ad creatives from an AI assistant: campaigns, image/video/UGC ads, brands, edits. | `https://mcp.adgpt.com/mcp` | 15 |
| [DatePhotos.AI](https://datephotos.ai) | Tinder, Hinge and Bumble photo rules and AI-photo policies, plus a free dating photo audit. | `https://datephotos.ai/api/mcp` | 3 |
| [Recao](https://recao.app) | Rank a competitor's EU App Store ads by longevity. From Apple's official Ad Repository. | `https://recao.app/api/mcp` | 17 |
| [Clypmint](https://clypmint.com/developers) | Edit videos with AI: cuts, captions, B-roll and motion in a style you pick or copy from any video. | `https://clypmint.com/mcp` | 37 |
| [mcp](https://budgetpixel.com/mcp) | Generate AI images, video, music, and sound effects, and upscale them, from any MCP client. | `https://mcp.budgetpixel.com/mcp` | 18 |
| [Duskly](https://duskly.ai/mcp-server) | MLS compliance for edited listing photos: classify edits, write disclosures, verify provenance. | `https://duskly.ai/mcp` | 10 |
| [CCAPI](https://ccapi.ai/mcp) | Image, video, music and text generation across 100+ models through one endpoint. | `https://api.ccapi.ai/mcp` | 11 |
| [kavel-mcp](https://www.kavel.ai) | Discover Kavel's AI photo/video generators, get tuned prompts, and open the right tool on kavel.ai. | `https://www.kavel.ai/api/mcp` | 4 |
| [captcha.cc Human Verification](https://captcha.cc/docs/mcp) | Human verification CAPTCHA with visual and selective-listening audio challenges. | `https://captcha.cc/mcp` | 3 |
| [AI Video Atlas](https://aivideoatlas.com/agents/) | Plan AI video shots: model picks, sourced prompts, prompting guides and real $/s costs. | `https://mcp.aivideoatlas.com/mcp` | 10 |

### Finance and crypto

| Server | What it does | URL | Tools |
|---|---|---|---|
| [NL Ledger](https://nlledger.ca/data/) | NL provincial and federal spending records, each with its source. Addresses do not locate work. | `https://nlledger.ca/mcp` | 15 |
| [CareRanks Data](https://careranks.com/docs/data/) | CMS quality ratings, payer-negotiated prices, and clinician data for 41K+ US healthcare facilities. | `https://careranks.com/mcp` | 5 |
| [CryptoPulse Data API](https://cryptopulse.saascloud.ai) | Pay-per-call crypto market intelligence for AI agents. USDC on Base via x402. | `https://cryptopulse.saascloud.ai/mcp` | 11 |
| [forms](https://bluecraneworks.ca/tools) | Canadian contractor forms + tax tools: 126 cited forms, sourced 2026 tax estimates by province. | `https://mcp.bluecraneworks.ca/mcp` | 8 |
| [BrokerFlat Forex Cashback](https://brokerflat.com) | Compare 11 forex brokers, calculate cashback per lot and get sign-up steps. Read-only, no login. | `https://mcp.brokerflat.com/mcp` | 4 |
| [Veliane Discovery Plus](https://velianediscoveryplus.aplusz.app/) | Facts, price, safety and join links for Veliane, free marriage-minded matchmaking. | `https://velianediscoveryplus.aplusz.app/mcp` | 7 |
| [Bankrolled.ai Agent Hub](https://bankrolled.ai/) | Free, sourced money facts and scheme lookups for US/UK/CA/AU/NZ. Answers cite bankrolled.com. | `https://bankrolled.ai/mcp` | 4 |
| [aikstockdata — Korean Stock Data](https://aikstockdata.com) | Korean stocks: median price path after each DART filing type, T+1 closes, earnings. 12 tools, no key | `https://mcp.aikstockdata.com/mcp` | 12 |
| [AHM Transfer](https://ahmtransfer.com/connector/) | Fixed prices, conditions and booking links for airport transfers in Alanya and Antalya, Türkiye. | `https://ahmtransfer.com/mcp` | 4 |
| [catalyst-edge-mcp](https://catalystedgescanner.com) | Audited SEC catalyst signals for agents — ranked filing intel with a public track record. | `https://catalystedgescanner.com/mcp/` | 7 |
| [StackRates VPS prices](https://stackrates.ai/ask/) | VPS prices read daily from providers' own pricing pages and APIs: cheapest by size, place or app. | `https://stackrates.ai/mcp` | 5 |
| [Besot: Musician Fashion Resale](https://besot.com) | Cross-source price compare for clothing musicians designed, wore, or founded. Real listings. | `https://mcp.besot.com` | 4 |
| [Dryos](https://www.dryos.ai/mcp) | Live US power market prices, load, generation, weather and permits for AI agents. | `https://api.dryos.ai/mcp` | 5 |
| [Brük — verified XRP Ledger answers](https://brukledger.com) | Verified XRP Ledger answers with proof: payment, send, and issuer checks. Pay per call via x402. | `https://bruk-agent-api.fly.dev/mcp` | 12 |
| [rocketsloth](https://rocketsloth.ai) | Website monetization for AI agents: apply, integrate ads, reporting, and payouts — all over MCP. | `https://rocketsloth.ai/mcp` | 14 |
| [Entervista](https://entervista.ai/developers) | Find and book local service businesses (plumbers, HVAC, detailers) at real prices, with approval. | `https://entervista.ai/mcp` | 14 |
| [FreelancerTax — Canadian self-employed tax math](https://freelancertax.ca) | Verified Canadian self-employed tax math: SE tax, CPP, GST/HST, instalments, CRA deadlines. Free. | `https://freelancertax.ca/mcp` | 6 |
| [Infrabase](https://infrabase.ai/mcp) | Hand-verified AI infrastructure directory: tools, alternatives, EU providers, LLM API prices. | `https://infrabase.ai/mcp` | 8 |
| [DABLOCK AI Visibility Index](https://dablock.ai/) | Measured share of answer for 24 crypto and Web3 brands. An open dataset, not an audit of your site. | `https://dablock.ai/mcp` | 5 |
| [Agentic Endpoints](https://agentic-endpoints.com) | Pay-per-call tools for autonomous agents, settled in USDC on Base via x402. | `https://agentic-endpoints.com/mcp` | 24 |
| [Bindler: UAE Corporate Tax, EU AI Act and CBAM calculators](https://bindler.co/mcp/) | Computes UAE Corporate Tax, EU AI Act risk class and CBAM cost, citing the Article behind each line | `https://bindler.co/mcp/rpc` | 3 |
| [LLM Hosting Pricing](https://llmhosting.ai/mcp-docs) | LLM and GPU rental prices: model price lookup, GPU listings, cheapest-GPU search, price history | `https://llmhosting.ai/mcp` | 5 |
| [mcp](https://birkinbagstock.com) | Live Hermes Birkin & Kelly market data: resale inventory, prices, auction calendar and results | `https://birkinbagstock.com/mcp` | 14 |
| [Relaystation](https://relaystation.ai) | Pay-per-call agent infrastructure: file storage & handoff, compute tools, messaging, e-sign, KYC. | `https://api.relaystation.ai/mcp` | 14 |
| [JustIdea Agency](https://justidea.agency/) | Services, prices, inquiries and free analytics, AI and Google visibility scans by JustIdea, Poland. | `https://justidea.agency/mcp` | 8 |

### Science, health and research

| Server | What it does | URL | Tools |
|---|---|---|---|
| [mcp](https://rxmanager.ai) | Live US drug acquisition costs (CMS NADAC) for AI assistants. Free, no auth, weekly data. | `https://mcp.rxmanager.ai/mcp` | 8 |
| [Andromeda Agent Lab](https://lab.ai-andromeda.com/?via=mcp-registry) | Research on how AI agents find the web: a daily task that's checked automatically, and a guestbook. | `https://lab.ai-andromeda.com/mcp` | 3 |
| [FRTracker — Federal Regulatory Research](https://frtracker.app/developers/mcp) | Source-linked US federal regulations: CFR provision history, obligations, rules, comments. | `https://frtracker.app/mcp` | 10 |
| [AdvisorIQ](https://advisoriq.com) | CE rules for US advisors by designation and state, plus independent wealth RIA data, with sources. | `https://mcp.advisoriq.com` | 13 |
| [DeepDNA](https://deepdna.ai/docs/#mcp) | Pharmacogenomics for AI agents: cited drug–gene, gene and rsID lookups plus a medication screen. | `https://deepdna.ai/mcp` | 6 |
| [Spoon Scout - Food Contaminant Lookup](https://food.agentlookups.ai/) | Lab results, FDA recalls and additive rules for US packaged foods, with sources; never a grade. | `https://food.agentlookups.ai/mcp` | 6 |
| [SuppCo](https://supp.co/developers) | Supplement research, product and brand TrustScores, and your SuppCo stack and Buying Club cart. | `https://api.supp.co/mcp` | 30 |
| [CutGPT Research & Fact-Check](https://cutgpt.app/mcp/) | Free fact-checks, papers, source vetting, plus verified AI pricing, comparisons, guides, and tools. | `https://mcp.cutgpt.app/mcp` | 14 |
| [mcp](https://github.com/buzzradr/mcp) | Live AI trend radar: trending AI topics, why-trending signals, daily digests. No API key. | `https://buzzradr.com/api/mcp` | 4 |
| [SHVL](https://shvl.app/?utm_source=mcp_registry&utm_medium=directory&utm_campaign=registry_20261016) | Review UK aged-debtors CSVs, workspace receivables briefs and saved case information. | `https://shvl.jlucwright.workers.dev/mcp` | 5 |
| [Invexia Stock Research](https://invexia.ai) | Free US stock research: snapshots, Titan Score valuation scorecards, 37 screeners, daily lists. | `https://invexia.ai/mcp` | 6 |
| [Appendix](https://appendix.com) | Physician-reviewed medical opinions and prescriptions for AI agents. | `https://mcp.appendix.com/mcp` | 3 |
| [WhichPost](https://whichpost.app/claude-and-chatgpt) | Which creator posts brought paying customers: your WhichPost reports, with ranges. | `https://whichpost.app/mcp` | 18 |
| [Frontier: evidence-scored science breakthroughs](https://frontierresearch.co) | New papers from Nature, Science, Cell, NEJM and other top journals, scored on evidence and novelty. | `https://frontierresearch.co/api/mcp` | 5 |
| [Zicron medical chronology (public)](https://claims.zicron.ai/for-ai-assistants) | Price, sample and request page-cited medical chronologies for law firms and LNCs. No sign-in or PHI. | `https://claims.zicron.ai/mcp` | 5 |
| [nullary](https://github.com/nullary-ai/nullary) | Negative results intelligence for drug discovery — query measured failures via MCP. | `https://mcp.nullary.ai/mcp` | 35 |
| [Cosmic Chemistry](https://cosmicchemistry.co/ai-app) | Free Vedic astrology: birth chart, dasha, Sade Sati, Saturn return, panchang, planetary hours. | `https://cosmicchemistry.co/mcp` | 13 |
| [Bob Research Tools](https://bob.assimilatethis.com/) | Paid web research, news, prediction-market evidence, company briefs and fact-checks (x402 USDC) | `https://bob.assimilatethis.com/mcp` | 8 |
| [OpenCancer](https://opencancer.ai/connectors) | Cancer patient expert: NCCN-grounded answers with sources, recruiting trials, and expert review. | `https://opencancer.ai/api/mcp` | 5 |
| [Altair](https://altairworld.com/mcp) | Free TradingAgents equity research reports and Altair pages; paid signals feed via x402 inside MCP. | `https://altairworld.com/mcp` | 5 |
| [AlgoMaker — quantitative trading strategy factory](https://algomakers.com) | Mine, validate and paper-trade quantitative trading strategies. The engine runs on your machine. | `https://algomakers.com/mcp` | 4 |
| [YieldLord · 包租公](https://baozugong.app/mcp-guide) | RENT-ranked covered-call, CSP & wheel income ideas, your positions & Greeks. Never places orders. | `https://baozugong.app/api/mcp` | 4 |
| [quantum-artificer](https://quantum-artificer.surewhynot.app) | Scientific compute for AI agents: symbolic, numerical, quantum, chemistry, ODE. Paid via x402. | `https://quantum-artificer.surewhynot.app/mcp` | 6 |
| [website](https://cuvo.co/developers) | Cuvo Health published site content and live discovery-call booking tools for AI agents. | `https://cuvo.co/mcp` | 9 |
| [Catalyst evidence graph](https://catalystproject.ai/connect) | Findings on what compounds and supplements do in the body, with evidence strength, quote and paper. | `https://catalystproject.ai/mcp` | 7 |

### Open data and government

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Al-Taswia Iraqi Law Research](https://www.al-taswia.com) | Read-only search of Al-Taswia's published Iraqi law articles. General information, not legal advice. | `https://al-taswia-iraqi-law-research.al-taswia.workers.dev/mcp` | 3 |
| [ADF: EU Tenders, EU Funding, EU Medicines, CVE KEV EPSS, EU CERT Advisories, Amsterdam Events](https://agentdatafeed.com) | EU tenders, funding and medicines, CVEs with KEV and EPSS, EU CERT advisories, Amsterdam events. | `https://agentdatafeed.com/mcp` | 3 |
| [AICasePredict](https://aicasepredict.com) | Search a large legal database of 325M+ US court records: cases, attorneys, judges and courts. | `https://aicasepredict.com/mcp` | 5 |
| [DABYTE AI Visibility Index](https://dabyte.ai/) | Measured share of answer for 20 SaaS brands. An open dataset, not an audit of your site. | `https://dabyte.ai/mcp` | 5 |
| [AgentNative: Public Data, Government Datasets, Federal Statistics & Official Records](https://cazimedia.com/agentnative/) | Normalized official data with provenance, aggregations, insights, free samples and agent access. | `https://agentnative.cazimedia.com/mcp/government-data` | 14 |
| [China Visa & Regulation Data](https://cnregwatch.com) | China visa-free eligibility by nationality and latest official regulation changes, with sources. | `https://cnregwatch.com/mcp` | 5 |
| [publicdata.au](https://publicdata.au/agents/#mcp) | Search, filter, count and sum Australian government open data, with every version kept. | `https://publicdata.au/mcp` | 12 |
| [AI Law Tracker](https://ai-law-tracker.com/developers) | Audited AI-regulation data: laws, bills, news and obligations across US, EU and 62 jurisdictions | `https://ai-law-tracker.com/mcp` | 30 |
| [California Court Deadlines](https://calcourtdeadlines.com) | Computes California state court deadlines and cites the code section behind every date. No API key. | `https://calcourtdeadlines.com/api/mcp` | 9 |
| [TrustAI Verification](https://trustailaw.com/verify) | Neutral referee for legal-AI output: flags orphan quotes and uncited claims. Not legal advice. | `https://trustailaw.com/api/mcp` | 4 |
| [mcp](https://botnotice.app/docs/api) | AI disclosure laws by business and state, each law in full, and a website AI-notice check. | `https://botnotice.app/mcp` | 4 |
| [Human for AI](https://yourhuman.ai/) | Ask a human for legal review, confirmation, a signature, or a physical-world act | `https://yourhuman.ai/mcp` | 3 |
| [japan-data-mcp](https://japan-data-mcp.netlify.app) | Japanese law, corporation & statistics data as MCP, normalized to English with source attribution. | `https://japan-data-mcp.netlify.app/mcp` | 4 |
| [CaseDaleel — UAE legal information](https://casedaleel.com) | Read-only UAE legal information: official routes, practical guides, free tools and FAQs. | `https://casedaleel.com/mcp` | 4 |
| [MissedTakes](https://missedtakes.co/ai-assistants) | Graded track records of NFL and election pundits: records, leaderboards, takes, game and race calls. | `https://missedtakes.co/api/mcp` | 9 |
| [visa-check](https://canienter.com) | Visa & entry requirements for 199 passports, cited to official sources and re-verified daily. | `https://api.canienter.com/mcp` | 3 |
| [legal-lookup](https://co-legal.be/agent) | Belgian and Dutch legal & fiscal lookups (KBO, VIES, ECLI, Justel, EUR-Lex) plus scans. 14 tools. | `https://agent.co-legal.be/mcp` | 14 |
| [چیستارا — Iranian Legal Corpus](https://hoghogh.ai) | Search Iranian statutes, court rulings, advisory opinions and circulars, with legal calculators. | `https://hoghogh.ai/mcp` | 23 |
| [LexGO Jobs](https://www.lexgo.be/developers) | Live Belgian and Luxembourg legal jobs. Unauthenticated. Send candidates to click_url. | `https://www.lexgo.be/mcp` | 6 |
| [Government Radar](https://www.govradar.ca/ai-plugin) | Official Canadian federal and provincial government news releases from the last 7 days. | `https://www.govradar.ca/api/mcp` | 3 |
| [El Tablero: Argentina economic data](https://eltablero.ar/docs) | Argentine economic statistics from official sources (BCRA, INDEC): FX, inflation, rates, reserves. | `https://eltablero.ar/api/mcp` | 7 |
| [site](https://bagsthatpay.com) | Bags That Pay: the site's own MCP server — dataset, enquiry, entities, listing (enquiry = a... | `https://bagsthatpay.com/mcp` | 32 |
| [Seamark](https://seamark.app) | Personal sailing voyage log: trips, legs, ships, crew and GPX tracks with honest statistics. | `https://seamark.app/mcp` | 13 |
| [Gouda Studios Agent Tools](https://gouda-studios-agent-tools.vercel.app) | Pay-per-result SAM.gov contracts, SEC EDGAR filings, USAspending awards and GLEIF LEI lookups. | `https://gouda-studios-agent-tools.vercel.app/mcp` | 8 |
| [Claim Done](https://claimdone.com.au/connect-your-ai-assistant/) | Australian legal documents drafted from your answers for a flat fee. Not a law firm. | `https://claimdone.com.au/mcp` | 8 |

### Business and marketing

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Black Label Real Estate Website MCP](https://blbestate.com/connect) | Search and read public Black Label Real Estate pages with source URLs. | `https://blbestate.com/mcp` | 12 |
| [HuntBoard](https://huntboard.ai/mcp/) | Search real, recent job postings from company career pages and ATS boards, scored for fit. | `https://huntboard.ai/mcp` | 4 |
| [VegvisAI guide](https://vegvis.ai/) | Open guide to businesses in any country, plus Norwegian public services and parties. Never ranks. | `https://vegvis.ai/mcp` | 5 |
| [LeadProof](https://leadproof.co/mcp/) | Verified local-business lead lists: quote, sample and order. Raw data via our Apify actors. | `https://leadproof.co/mcp` | 6 |
| [Crevio](https://crevio.co) | An AI agent that runs your online business: products, orders, customers, email, and sites. | `https://mcp.crevio.co/mcp` | 18 |
| [Porch](https://porch.okibi.ai) | Public URLs for AI agents to catch webhooks, OAuth redirects, job callbacks and approval clicks. | `https://porch.okibi.ai/mcp` | 10 |
| [Commercial Garage Doorman](https://www.commercialgaragedoorman.ca/) | Commercial Garage Doorman, Hamilton area commercial door service: business facts and site search. | `https://www.commercialgaragedoorman.ca/mcp` | 3 |
| [tolca](https://tolca.tonbot.ca) | Verify a company before paying it: OFAC sanctions, UK/Canada registries, contractor licences (x402) | `https://tolca.tonbot.ca/mcp` | 11 |
| [Garage Doorman](https://www.garagedoorman.ca/) | Garage Doorman, Grimsby ON residential garage door repair: business facts, site search, quotes. | `https://www.garagedoorman.ca/mcp` | 4 |
| [Cobalt Capture](https://cobaltcapture.com/developers) | Annotated-screenshot reviews and ready-made product studies your AI agent can read, run, and share. | `https://cobaltcapture.com/mcp` | 12 |
| [Rooster Agent Gateway](https://roosteragents.ai/arsenal/rooster-agent-gateway/) | Discover, read and book verified real-world businesses through one endpoint. | `https://roosteragents.ai/mcp` | 3 |
| [coExploro](https://coexploro.com/mcp) | Read coExploro product teardowns: overall, UX and persona scores and top findings. | `https://api.coexploro.com/mcp` | 5 |
| [seo-audit](https://inxy.ai/mcp) | Free SEO & AI-search (AEO) audits for any site or Shopify store, with emailed weekly score reports. | `https://inxy.ai/api/mcp` | 5 |
| [Signal Leads](https://leads.cloudforbots.com) | 25 sales leads with a public funding, hiring or tech signal, source link and draft message each. | `https://leads.cloudforbots.com/mcp` | 3 |
| [China Industry Intel](https://mcp.chinaindustryintel.com/developers/mcp/) | Read-only selected China industry article excerpts, disclosed sources and company identity links. | `https://mcp.chinaindustryintel.com/mcp` | 3 |
| [TEK BOSS Small Business AI Strategy Assessment](https://github.com/M2201/TEKBOSS) | AI strategy, workflow automation, and process-improvement assessment for small businesses. | `https://tekboss.ai/mcp/assessment` | 3 |
| [AGORA Omega](https://agoraverify.com) | Pay-per-call checks for AI agents: sanctions, MiCA, French KYB, AI Act. USDC via x402. | `https://agoraverify.com/mcp` | 8 |
| [proofstack](https://github.com/lttxzmj/proofstack-mcp) | Audited indie product business cases with source-backed pricing, revenue and pricing benchmarks. | `https://proof-stack-lake.vercel.app/mcp` | 3 |
| [Vaeo AI Discovery Reports](https://vaeo.com.au/agents) | How often AI assistants name a local Australian business, and which pages they read. | `https://vaeo.com.au/mcp` | 7 |
| [gethal.ai](https://gethal.ai) | Public MCP for gethal.ai — autonomous AI sales agent. Pricing, features, book a demo. | `https://gethal.ai/mcp` | 7 |
| [GoodLeads](https://goodleads.club) | Find new business owner contacts the morning the state posts a filing. Preview free, pay per record. | `https://mcp.goodleads.club/mcp` | 14 |
| [Agentic Dealer Network](https://agenticdealernetwork.com) | Live franchised-dealer inventory, quotes, and consented salesperson handoffs. | `https://gateway.agenticdealernetwork.com/mcp` | 12 |
| [usedby](https://www.usedby.ai/developers) | Which companies publicly use which AI and software tools, each line with its public source. | `https://www.usedby.ai/mcp` | 5 |
| [Earlywire — Marketing & Growth Intelligence](https://earlywire.barisasa.com) | Marketing, growth & SEO intel: 120+ practitioner sources, judged daily, with citable summaries. | `https://earlywire.barisasa.com/mcp` | 6 |
| [BizValueDash](https://bizvaluedash.com/ai-connector) | Estimate what a small business is worth and search plain-English valuation guides. Read-only. | `https://bizvaluedash.com/mcp` | 3 |

### AI, agents and memory

| Server | What it does | URL | Tools |
|---|---|---|---|
| [MemoryRouter](https://memoryrouter.ai) | Persistent AI memory shared across Claude, ChatGPT, coding agents, and compatible MCP clients. | `https://mcp.memoryrouter.ai/mcp` | 10 |
| [makememoneynomistakes.ai: ERC-8004 agent reputation and fraud checks](https://makememoneynomistakes.ai) | Check before you hire or pay an ERC-8004 agent on Base: track record, reputation and fraud flags. | `https://makememoneynomistakes.ai/mcp` | 15 |
| [RFix](https://rfix.ai) | Create RF signal projects from prompts, inspect graphs, and export IQ data. | `https://mcp.rfix.ai/mcp` | 6 |
| [AI Deals Sentinel: Free AI API Tiers](https://ai-deals.rockpool.cc) | Agent-operated. Free LLM, GPU, search and embedding API tiers: limits, dated, linked to the source. | `https://ai-deals.rockpool.cc/mcp` | 3 |
| [zRev AI](https://www.zrev.ai/mcp) | Grade any llms.txt, cold-read a homepage, run a B2B GTM ROI model, get a GTM diligence checklist. | `https://go.zrev.ai/mcp` | 9 |
| [Daishi](https://daishi.ai) | A persistent multi-agent world any AI agent can join over MCP, with a public record of every match. | `https://daishi.ai/mcp` | 35 |
| [Sugra API](https://github.com/Sugra-Systems/sugra-api-mcp) | Gateway between LLM agents and world data through eight tools and a bundled endpoint catalog. | `https://app.sugra.ai/mcp` | 11 |
| [ctxstore — memory that follows you across models](https://ctxstore.ai) | Persistent memory for AI agents: keyed facts, a wake bundle each session, one memory in every model. | `https://mcp.ctxstore.ai/mcp` | 31 |
| [promptsharp](https://promptsharp.ai/mcp-setup) | Professional prompt library over remote MCP: 13 verticals, free discovery scope. | `https://promptsharp.ai/mcp` | 3 |
| [WorkingMemory](https://workingmemory.ai) | Persistent personal memory for AI assistants — save, search, and recall across every MCP client. | `https://app.workingmemory.ai/mcp` | 4 |
| [Proofsource](https://proofsource.co/ai-assistants) | AI visibility: which buyer questions name your brand in ChatGPT, Perplexity, Claude, AI Overviews. | `https://app.proofsource.co/v1/mcp` | 14 |
| [The Aggregate — LLM benchmark aggregate](https://theaggregate.ai/mcp) | LLM rankings from public benchmarks, model comparisons and source-linked results. Updated daily. | `https://theaggregate.ai/mcp` | 8 |
| [CatchUI](https://catchui.com/mcp) | What is this UI element called? 50 curated UI patterns, names per platform, build prompts. EN/中文. | `https://catchui.com/api/mcp` | 6 |
| [mcp](https://cheapestinference.com) | Discover unlimited LLM inference pools, get USDC quotes, subscribe on Base, check key status. | `https://api.cheapestinference.com/mcp` | 7 |
| [LLM API Pricing and Automation Tools by shurco.ai](https://shurco.ai/tools/llm-api-pricing/) | Daily LLM API prices, cost estimates and automation ROI tools from shurco.ai | `https://shurco.ai/mcp` | 10 |
| [ActableSite AI Crawler Monitor](https://actablesite.com/mcp-server) | Check AI crawler robots.txt policy and monitor public-site policy, sitemap, and llms.txt changes. | `https://actablesite.com/mcp/` | 5 |
| [LLMIntel Model Lifecycle](https://llmintel.ai) | Check whether an LLM model id is deprecated, retiring, or retired, and what to migrate to. | `https://llmintel.ai/v1/mcp` | 5 |
| [reviewpaper.ai](https://reviewpaper.ai/developers) | Review forms for 29 ML/NLP/CV venues, AI conference deadlines and ICLR acceptance odds. | `https://reviewpaper.ai/mcp` | 7 |
| [AUN — Agent Upgrade Network](https://a-upgradenet.com) | Audit AI agents' tool calls, planning and memory; Base on-chain data; pay per call via x402. | `https://a-upgradenet.com/mcp` | 6 |
| [Race Calendar F1](https://racecalendar.app/f1) | Anonymous read-only Formula 1 tools, resources, prompts, completion, and interactive dashboard. | `https://racecalendar.app/mcp` | 15 |
| [Promise](https://www.usepromise.ai/mcp) | Evidence-backed follow-through memory for what you owe, await, and need to remember. | `https://mcp.usepromise.ai/mcp` | 11 |
| [ENYAL by Greenland AI](https://enyal.ai) | ENYAL by Greenland AI — encrypted identity & memory for AI agents (query, recall, provenance) | `https://mcp.enyal.ai/mcp` | 9 |
| [Penny](https://mypenny.ai) | Portable AI memory you own. Keep memories and notes across Claude, ChatGPT, and other AI tools. | `https://app.mypenny.ai/mcp` | 7 |
| [Cite Files](https://citefiles.com/integrations) | Check whether AI assistants can reach, read and cite a public website. No account for 4 of 5 tools. | `https://citefiles.com/mcp` | 5 |
| [core.blue](https://core.blue/) | Private, self-describing memory for agents: one house per customer, on a machine of its own. | `https://mcp.core.blue/` | 10 |

### Utilities

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Navigi: community services across Canada](https://navigi.ca) | Community services in every Canadian community, each with the date it was last checked. | `https://api.navigi.ca/v1/mcp` | 4 |
| [BackPow PoW Oracle](https://backpow.com) | Proof of Work oracle: solo mining odds, cost of production, hashrate, mining hardware | `https://mcp.backpow.com/mcp` | 6 |
| [BookTheTee Golf Tee Times](https://bookthetee.com) | Find public golf courses near NYC and get official tee-time booking links. | `https://bookthetee.com/mcp` | 3 |
| [530A Model calculator](https://530amodel.com/api) | Free, deterministic 530A (Trump Account) projections, verified rules, and searchable guides. | `https://mcp.530amodel.com` | 4 |
| [Alternative Asset Literacy — Retail](https://github.com/untitledfinancial/aal-plugins) | Alternative-asset education for retail investors: deep-dive tracks, calculators, advisor lookup. | `https://alternativeassetliteracy.com/mcp/retail` | 22 |
| [Powerline Email Tools](https://powerline.ai/tools/) | Email deliverability checks: SPF, DKIM, DMARC, BIMI, MTA-STS, blacklists, headers, spam words | `https://powerline.ai/mcp` | 5 |
| [AstraVerify Domain Trust Check](https://astraverify.com/connect) | Email security and AI discoverability scores for any domain, with the exact record or tag to fix. | `https://astraverify.com/mcp` | 5 |
| [CELPass: CELPIP practice and CRS calculator](https://celpass.com/mcp-server) | CELPIP practice questions with answers, sample answers, and Canada's November 2026 CRS calculator. | `https://celpass.com/mcp` | 5 |
| [Church Year](https://crossandcovenant.co/church-year-connector) | Western church year: seasons, colors, feasts, Easter and Pascha, and the 1979 BCP Sunday lectionary. | `https://crossandcovenant.co/api/mcp/church-year` | 4 |
| [The Automators](https://theautomators.ai/mcp/) | Read-only MCP server for The Automators: services, pricing, industries, case studies, calculators. | `https://mcp.theautomators.ai/mcp` | 18 |
| [Surf Hut](https://aisurfhut.com) | Signed proof-of-time, 30-day stash, live NOAA surf data. No auth. The hut keeps honest clocks. | `https://aisurfhut.com/mcp` | 4 |
| [Optionscanner](https://optionscanner.ai/learn/mcp) | Free options calculators and the Optionscanner Learn library for any AI assistant. No account. | `https://optionscanner.ai/mcp` | 10 |
| [ChangeThisFile](https://changethisfile.com) | 1,000+ conversion routes plus translate, extract tables, compress. 25 free/month, then a free key. | `https://changethisfile.com/mcp` | 7 |
| [leafwright](https://leafwright.co) | Render HTML, URLs, and templates to PDF. AI drafts templates and fixes them from logs. | `https://leafwright.co/mcp` | 3 |
| [MainBook Bank Statement Converter](https://mainbook.ai/mcp) | Convert PDF bank statements to checked Excel, CSV or JSON with balance validation. | `https://mcp.mainbook.ai/mcp` | 4 |
| [SparkQuote NEC calculators](https://sparkquote.ai/tools/mcp-server) | NEC 2023 electrical calculators: wire size, ampacity, voltage drop, conduit fill, box fill, load. | `https://sparkquote.ai/mcp` | 10 |
| [Star Wars MCP](https://swapi.build) | Star Wars API (SWAPI) as a remote MCP server: films, people, planets, species, starships, vehicles. | `https://swapi.build/mcp` | 4 |
| [The Dinner Table Club](https://www.thedinnertable.club/connect) | Find The Dinner Table Club dinner parties for strangers in NYC, DC, LA and Miami by city and date. | `https://www.thedinnertable.club/mcp` | 3 |
| [Best Time to Book Hotels](https://www.besttimetobookhotels.com/mcp) | Best-time-to-book verdicts, live last-minute hotel deals, and city price calendars, from data. | `https://www.besttimetobookhotels.com/api/mcp` | 6 |
| [mcp](https://swiftsign.ca) | E-signatures for agents: mint a sandbox key, send PDFs, track status, download the sealed result. | `https://swiftsign.ca/mcp` | 10 |
| [mcp](https://candidcost.com/for-agents) | Cited, receipt-backed US home-buying data & calculators — education-only, every number sourced. | `https://candidcost.com/api/mcp` | 10 |
| [IronLedger strength calculators](https://www.ironledger.app/tools) | Free strength-training calculators, plus a checker for program files you import into IronLedger. | `https://www.ironledger.app/mcp` | 7 |
| [SendaFax](https://sendafax.ai) | Send a fax in Australia (+61). Pay only if it delivers. Email receipt. No card at send. | `https://sendafax.ai/api/mcp` | 3 |
| [HomeCalc — Canadian Mortgage & Tax Calculators](https://homecalc.ca/connector) | Canadian mortgage, tax & land transfer calculators: 12 read-only tools, LTT for all 13 provinces. | `https://homecalc.ca/api/mcp` | 12 |
| [Prince Cloud](https://prince.cloud) | Convert Markdown, HTML, and web pages to high-quality PDF with Prince. | `https://prince.cloud/mcp` | 3 |

### Other

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Ashraf Gents Hostel, Kalamassery](https://ashrafgentspghostel.adserr.com) | Men's hostel in Kalamassery, Kochi: facts, rates, local guides, nearby places, WhatsApp enquiry. | `https://hostel-mcp.adserr.com/mcp` | 5 |
| [LaunchTrust](https://github.com/mustafasalimerek-bit/launchtrust-mcp) | Compliance & security scan for your app: secrets, exposed files, headers, privacy, AI-disclosure. | `https://mcp.launchtrust.co/mcp` | 9 |
| [Fidenta Verify](https://verify.noevant.ai) | Independent fact-checking for AI answers: a verdict and sources for every claim. | `https://verify.noevant.ai/mcp` | 5 |
| [Catalogue APP24, formations d'échecs en français](https://boutique.apprendre-les-echecs-24h.com/) | 94 formations d'échecs en français, prix à jour, conseil d'entraîneur. French chess courses. | `https://mcp.apprendre-les-echecs-24h.com/` | 7 |
| [Wireless Choices Plan Finder](https://wirelesschoices.com.au/tools/ai-assistants) | Compare Australian mobile, prepaid, mobile broadband and nbn plans listed on Wireless Choices | `https://mcp.wirelesschoices.com.au/mcp` | 4 |
| [seoul-apt-signal](https://airblockfz.com) | Seoul apartment signals: 25 districts from official transactions, scans. Pay-per-call x402. | `https://seoul-apt-signal.airblock2026.workers.dev/mcp` | 6 |
| [CarePlanKit — Nursing Care Plans](https://careplankit.com/) | Nursing care plans for students: diagnoses, SMART goals, interventions with rationale, sources. | `https://mcp.careplankit.com/mcp` | 3 |
| [verify](https://www.sickslip.co/verify) | Verify a SickSlip doctor's note by Document ID; states served, pricing, physician NPI. Read-only. | `https://sickslip.onrender.com/api/mcp` | 5 |
| [rssa](https://github.com/getvda-ai/rssa) | Read, verify and validate RSS-A signed agent feeds and groups (RSS for Agents). | `https://hub.rssa.getvda.ai/mcp` | 3 |
| [Artemisia · Aguas SB](https://aguassb.com/artemisia/) | Orientación sobre agua de pozo, vertidos y reutilización, con lo publicado por Aguas SB. | `https://artemisia.comercial-asb-sl.workers.dev/mcp` | 6 |
| [WOCLUB Cube Playground](https://github.com/timememe/woclub) | Shared voxel world for AI agents. Extend First Light at the world centre over HTTP or MCP; no auth. | `https://worldorder.club/mcp` | 12 |
| [SerialHunt](https://bigballi.com/SerialHunt/connect) | US bill serial numbers: star note print runs and fancy serial patterns with exact odds. | `https://bigballi.com/SerialHunt/mcp` | 4 |
| [Paylyte](https://paylyte.ai/connect) | Agent Trust Score earned through Proof of Outcome. Browse and buy as paylyte-core. | `https://api.paylyte.ai/mcp` | 3 |
| [agi-scorecard](https://agiscorecard.com) | 8 graded AGI-2027 predictions, the 0-100 Thesis Tracker, and a public market-call ledger. Free. | `https://agiscorecard.com/mcp` | 8 |
| [AFMR Discovery](https://afmr.ai/) | Read AFMR failure modes and discover scoped attestation and lift-evidence contracts. | `https://afmr.ai/mcp` | 4 |
| [Eggtimer.app](https://eggtimer.app) | Shareable timer links for countdowns, clock times, Pomodoro, Tabata and step recipes. No account. | `https://eggtimer.app/api/mcp` | 7 |
| [Flaim Fantasy](https://flaim.app) | Fantasy analysis for your ESPN, Yahoo, and Sleeper leagues. Reads your leagues, never changes them. | `https://api.flaim.app/mcp` | 11 |
| [indexnow-toolkit](https://aiwebsitepipeline.com/method.html) | Build and validate IndexNow payloads, check key files, and diff sitemaps into a submission list. | `https://indexnow-toolkit-mcp.lipmichal.workers.dev/mcp` | 3 |
| [Latzerus Lernbereich](https://www.latzerus.ch) | Latzerus (CH): 100+ kostenlose 5-Minuten-Lernmodule zu Vertrieb, KI und Karriere. | `https://mcp.latzerus.ch/mcp` | 4 |
| [Licensed House Painters](https://github.com/modelcontextprotocol/registry) | Find licensed house painters in 11 US states, with dated license status from state boards. | `https://house-painters.ottobot.agency/mcp` | 3 |
| [Dreamlit](https://github.com/dreamlit-ai/dreamlit-mcp) | Create, test, publish, and manage Dreamlit notification workflows from AI clients. | `https://mcp.dreamlit.ai/mcp` | 12 |
| [AI Signals (Signals API)](https://github.com/jiangzhangcc-glitch/signals-api-mcp) | Daily AI signals for agents: today's 4 signals, what changed, ranked models and repos | `https://data.jiangzhang.ca/signals4/mcp` | 5 |
| [facesign-mcp](https://docs.facesign.ai/docs/mcp) | Build and test FaceSign step-up verification flows from your AI coding tool | `https://mcp.facesign.ai/mcp` | 5 |
| [scrypta-mcp-server](https://scrypta.com.br) | Scrypta MCP Server — Infraestrutura de visibilidade para Agentes de IA. | `https://scrypta.com.br/mcp` | 6 |
| [WOD Coach: AI Personal Trainer](https://wod-api-production.up.railway.app/llms.txt) | Fitness MCP: AI personal trainer, workouts, injury exercise swaps, race pacing. Pay-per-call x402. | `https://wod-api-production.up.railway.app/mcp` | 7 |

## Method

1. `scripts/fetch_registry.py` reads every server (latest version) from the registry and keeps remote endpoints.
2. `scripts/probe.py` tests Streamable HTTP endpoints that need no headers, at most 5 URLs per host, no temporary tunnels, 10 s timeout.
3. `scripts/make_directory.py` drops mass-generated copies (same tool set more than 3 times, same description more than twice, more than 2 per domain) and assigns topics by keyword.

The workflow in `.github/workflows/weekly.yml` runs this every Monday and commits the result. Data: CC BY 4.0. Code: MIT.

Maintained by [Shortform Kit](https://shortformkit.com), which runs its own free remote MCP server for social video transcripts and creator data: `https://shortformkit.com/mcp`.

