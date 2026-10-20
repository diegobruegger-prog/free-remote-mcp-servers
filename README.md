# Free remote MCP servers (tested weekly)

Remote [Model Context Protocol](https://modelcontextprotocol.io) servers from the [official MCP Registry](https://registry.modelcontextprotocol.io) that answer **without any API key, token or login**. Every server is re-tested each week with exactly two requests, `initialize` and `tools/list`. No tool is ever called.

**Last run: 2026-10-19** · 18,301 endpoints tested · **10,520 open (57 %)** · 5,688 need auth · 2,093 not working · 8,581 listed after removing copies

- Tool annotations (as declared by the servers, not verified): 3,532 of 10,514 open servers annotate none of their tools. Of 119,049 tools, 83,867 carry annotations, 64,331 say readOnlyHint true, 6,309 say destructiveHint true. Per server in the `tools_annotated`, `tools_read_only` and `tools_destructive` columns. Note: we only see the tools a server lists without a key.
- Full list: [`data/servers.csv`](data/servers.csv) and [`data/servers.json`](data/servers.json)
- Browse with search and topics: [shortformkit.com/free-remote-mcp-servers](https://shortformkit.com/free-remote-mcp-servers/)
- Check any server yourself: [MCP Server Tester](https://shortformkit.com/mcp-server-tester/)
- Analysis with charts (failure reasons, hosting, tool counts): [State of remote MCP servers 2026](https://shortformkit.com/state-of-remote-mcp-servers-2026/)
- Key numbers with dates, ready to cite: [MCP statistics 2026](https://shortformkit.com/mcp-statistics/)

## Add a server to your client

| Client | How |
|---|---|
| Claude (claude.ai, desktop) | Customize, Connectors, + Add, Add custom connector, paste the URL |
| Claude Code | `claude mcp add --transport http NAME URL` |
| Cursor | `{"mcpServers": {"NAME": {"url": "URL"}}}` in `~/.cursor/mcp.json` |
| VS Code | `{"servers": {"NAME": {"type": "http", "url": "URL"}}}` in `.vscode/mcp.json` |

## Is your server in the list?

Show its live status in your README. The badge re-tests the endpoint about once an hour (same two read-only requests) and links to the full test result:

```markdown
[![MCP status](https://shortformkit.com/api/mcp-badge?url=YOUR_URL_ENCODED)](https://shortformkit.com/mcp-server-tester/?url=YOUR_URL_ENCODED)
```

Replace `YOUR_URL_ENCODED` with your endpoint, URL-encoded, or run the [MCP Server Tester](https://shortformkit.com/mcp-server-tester/) once and copy the ready-made badge from the result.

## Picks by topic

Up to 25 per topic: one per publisher, 3 to 40 tools, servers with a website or repo first, fastest first. Open means usable without signing up, not an endorsement: read what a server does before you connect it.


### Search and web

| Server | What it does | URL | Tools |
|---|---|---|---|
| [openlibrary-mcp-server](https://github.com/cyanheads/openlibrary-mcp-server) | Search books and authors, fetch editions, browse subjects, and resolve cover images. | `https://openlibrary.caseyjhand.com/mcp` | 10 |
| [EcoAloha](https://ecoaloha.com/developers) | Search and compare outdoor experiences. Public keyless API; booking and payment happen on Viator. | `https://ecoaloha.com/mcp` | 12 |
| [merchantwords](https://www.merchantwords.com/developers/mcp) | Amazon keyword volume, reverse-ASIN, and SERP data across 11 marketplaces. | `https://mcp.merchantwords.com/mcp` | 7 |
| [Chinaready China Market-Entry Search](https://chinaready.co/docs/api/) | Read-only search over chinaready.co — China market entry for Western software teams. | `https://mcp.chinaready.co/mcp` | 3 |
| [Socketlist](https://socketlist.pages.dev/mcp-server/) | Search a directory of 800+ open-source MCP servers: find, compare and get install configs. | `https://socketlist.pages.dev/mcp` | 4 |
| [Answering Service Care](https://answeringservicecare.com/developers/) | Read-only facts about Answering Service Care: company info, services, pricing, site search. | `https://answeringservicecare.com/mcp` | 5 |
| [intentlink](https://intentlink.io) | The best agent monetization tool: free search, clear rev-share, 10M+ commerce/travel/local offers. | `https://api.intentlink.io/mcp/` | 3 |
| [GTH Intelligence - Substance Abuse Treatment Finder](https://github.com/Crindo2/gth-mcp-server) | Search 12,338 curated, SAMHSA-sourced addiction treatment facilities across all 50 US states. | `https://gth-mcp-server.pages.dev/mcp` | 4 |
| [ai-visibility](https://ai-visibility.lastminutedealshq.com/?src=mcp-registry) | AI-search-visibility tools: check crawler access, generate llms.txt, lint robots.txt, census data. | `https://ai-visibility.lastminutedealshq.com/mcp` | 4 |
| [SEC EDGAR Filings MCP](https://github.com/stagproject/sec-filings-mcp) | SEC EDGAR MCP: search, preview, purchase filings. x402 USDC on Polygon. xpay + Cloud Run upstream. | `https://sec-filings-mcp-1065601264332.us-central1.run.app/mcp` | 3 |
| [Insurers Global](https://insurers.global) | Search the world's licensed insurers by country, class, group and regulator. Read-only, no auth. | `https://insurers.global/mcp` | 14 |
| [BrokerIA Imoveis](https://github.com/raklapimenta/brokeria-mcp-server) | Search Brazilian real estate, simulate financing, qualify leads, schedule visits. | `https://mcp.brokeria.com.br/mcp` | 8 |
| [DoorProfit Crime & Neighborhood Data](https://api.doorprofit.com) | US crime scores, incidents, neighborhood demographics, rent data, and offender search by address. | `https://api.doorprofit.com/mcp` | 4 |
| [Web Search & Data API](https://api.kadec0.xyz/docs) | Web search, scraping, Google Trends and data lookups. Paid per call in USDC on Base via x402. | `https://api.kadec0.xyz/mcp` | 23 |
| [Velven](https://velven.ai/docs) | Publish browser games, worlds, tools and wonders built with AI to Velven's hosting, and manage them. | `https://mcp.velven.ai/mcp` | 5 |
| [Helium MCP Server - News, Markets & AI](https://heliumtrades.com/mcp-page/) | Real-time news with bias scoring, live market data, and AI-powered options pricing | `https://heliumtrades.com/mcp` | 10 |
| [AegeanBot Direct Stays](https://aegeanbot.com/mcp/) | Search verified Greek vacation rentals with live availability, prices, policies, and booking links. | `https://app.aegeanbot.com/mcp` | 5 |
| [4dayweek.io Jobs](https://4dayweek.io/mcp) | Search reduced-hours jobs and employers: 4-day weeks, 9-day fortnights, half-day Fridays and more. | `https://4dayweek.io/api/mcp` | 6 |
| [Employment Lawyers Group](https://worklawyerca.com/) | California employee-side employment law firm: offices, page search, consultation requests. | `https://admin.worklawyerca.net/public/agent/mcp.php` | 5 |
| [Unlisted Property Search](https://unlistedhomes.com) | Search and explore residential properties that aren't for sale (yet) | `https://api.unlistedhomes.com/mcp` | 3 |
| [MCP Automations](https://github.com/wzltmp/mcp-automations) | Summarize URLs, repurpose content, daily news digests, find competitors. Cost telemetry built in. | `https://mcp-automations.fly.dev/mcp` | 4 |
| [Learn the Dao — Tao Te Ching](https://learnthedao.com) | Read, search and cite all 81 chapters of the Tao Te Ching, with per-rendering attribution. | `https://learnthedao.com/api/mcp` | 4 |
| [Docket Nexus](https://docketnexus.com) | Search public U.S. federal litigation: companies, cases, dockets and document metadata. | `https://mcp.docketnexus.com/mcp` | 6 |
| [Hex.pm MCP](https://github.com/joshrotenberg/hexpm-mcp) | MCP server for hex.pm and hexdocs.pm: search, inspect, compare, and audit Elixir packages | `https://hexpm-mcp.fly.dev/mcp` | 24 |
| [Not Human Search](https://nothumansearch.ai) | Search the agentic web. 4,100+ sites, 11 tools incl. check_url + verify_mcp for probe-before-use. | `https://nothumansearch.ai/mcp` | 14 |

### Documentation and knowledge

| Server | What it does | URL | Tools |
|---|---|---|---|
| [nyuchi-docs](https://docs.nyuchi.com/integrations/docs-mcp/) | Search, read, and ask the Nyuchi docs (docs.nyuchi.com); send feedback or raise issues. | `https://docs.nyuchi.com/mcp` | 5 |
| [Meeba Brain](https://github.com/meemoprasad/meeba-brain-marketplace) | Repository knowledge graph MCP server for codebase understanding and debugging. | `https://meeba-context-mcp-469248886325.us-central1.run.app/mcp` | 5 |
| [draw.io](https://www.drawio.com) | Create draw.io diagrams in chat from Mermaid or XML, shown live and interactive. 10,000+ shapes. | `https://mcp.draw.io/mcp` | 3 |
| [VetAid — VA Claim Intelligence](https://vetaid.ai) | Real Board of Veterans' Appeals outcome data for VA disability claims. No key needed. | `https://vetaid-mcp.onrender.com/mcp` | 9 |
| [Resemble AI](https://github.com/resemble-ai/resemble-mcp) | Resemble AI: deepfake detection, media intelligence, and watermarking actions, plus docs tools. | `https://mcp.resemble.ai/mcp` | 18 |
| [Andrii Co. Notary & Apostille Assistant](https://andrii.co) | Book a Washington notary or apostille appointment, get a quote, and track it, via AI assistant. | `https://andrii.net/mcp` | 15 |
| [MarketCheck API Docs](https://developers.marketcheck.com/mcp) | MarketCheck API docs for coding assistants: search, endpoint reference, plans. Free, no auth. | `https://developers.marketcheck.com/api/docs-mcp` | 5 |
| [agent-door](https://measuretechpro.com) | The full CRM for contractors, asked directly: crew pricing, knowledge base, forum, roadmap. | `https://measuretechpro.com/mcp` | 13 |
| [Cited](https://entradox.github.io/cited-site/) | AI-answer-engine visibility scans for local businesses, as agent tools | `https://cited-api-production.up.railway.app/mcp/` | 9 |
| [Coverage Cat](https://www.coveragecat.com) | Get umbrella and homeowners insurance quotes, select a policy, and bind coverage. | `https://www.coveragecat.com/api/consumer/mcp` | 23 |
| [Microsoft Learn MCP](https://github.com/MicrosoftDocs/mcp) | Official Microsoft Learn MCP Server – real-time, trusted docs & code samples for AI and LLMs. | `https://learn.microsoft.com/api/mcp` | 3 |
| [BIS — Butkeraites Intelligent Solutions](https://bisdecisions.com) | AI + optimization consultancy: how BIS solves operational decisions and beats alternatives. | `https://bisdecisions.com/api/mcp` | 8 |
| [UDS Toolbox](https://udslib.com/mcp.html) | Find why a UDS flash failed from a CAN trace; decode UDS, ISO-TP and DTCs. No hardware. | `https://mcp.udslib.com/mcp` | 7 |
| [Axint](https://github.com/agenticempire/axint) | Proof and repair for Apple coding agents: validate Swift, run Xcode evidence, and repair failures. | `https://mcp.axint.ai/mcp` | 36 |
| [AutEng Docs — Agent Document Workspace & Publishing](https://auteng.ai) | Agent document workspace with wallet auth. Create, update and share markdown docs. By AutEng.ai | `https://auteng.ai/mcp/docs` | 6 |
| [capacitor-mcp](https://capawesome.io/) | Unofficial MCP server for the Capacitor documentation, plugin list and blog. | `https://capacitor-mcp.capawesome.io/mcp` | 4 |
| [Kingy Guides](https://kingy-guides.vercel.app/) | Game guides from kingy.wiki: sourced answers, one-level hints and credited exact video moments. | `https://kingy-guides.vercel.app/mcp` | 4 |
| [Tyton](https://usetyton.com) | Audit and set up Meta Pixel and the Conversions API from your AI agent. | `https://mcp.usetyton.com/mcp` | 27 |
| [pody-mcp](https://pody.io/mcp) | Israeli podcast & content marketplace MCP — 7 tools: studios, podcasts, glossary, industry report. | `https://pody.io/api/mcp` | 7 |
| [Absolute value sign, number discarded](https://github.com/sadri-dridi/named-mcp-utilities) | Absolute value sign, number discarded | `https://agent-observatory-sensor.nolimit-observatory.workers.dev/s/abs-ok/mcp` | 31 |
| [RuneScape Wiki](https://runescape-wiki-mcp.fly.dev) | RS3 Grand Exchange prices, item lookup, player hiscores, and RuneScape Wiki content | `https://runescape-wiki-mcp.fly.dev/mcp` | 12 |
| [FreeRateUpdate Mortgage & Home Equity Shopping](https://www.freerateupdate.com/mortgage-home-equity-mcp) | Today's mortgage and home equity rates (HELOC, home equity loan, cash-out), lenders, start links. | `https://fru-api.freerateupdate.com/mcp` | 10 |
| [Arcology Knowledge Node](https://lifewithai.ai/mcp) | Collaborative engineering KB for a mile-high city. 9 tools, 8 domains, 32 entries. | `https://arcology-mcp.fly.dev/mcp` | 9 |
| [failmodes](https://github.com/elyngved/failmodes-mcp) | MCP server for the Fail Modes taxonomy — a knowledge base of AI system failure modes | `https://www.failmodes.com/api/mcp` | 4 |
| [Vector Panda Documentation](https://www.vectorpanda.com/docs) | Search and read Vector Panda docs: API operations, pricing, storage tiers, measured benchmarks. | `https://www.vectorpanda.com/mcp` | 8 |

### Developer tools

| Server | What it does | URL | Tools |
|---|---|---|---|
| [DAITK (Dibblee AI Tool Kit) - Total Import Cost](https://daitk-tic.dibind.com) | Import duty into Canada only. By HS code and origin: tariff, surtax, quota, anti-dumping. | `https://daitk-tic.dibind.com/mcp` | 6 |
| [Hydrata - ANUGA Flood Simulation](https://github.com/Hydrata/hydrata-mcp-server) | Run ANUGA flood simulations, track progress, and retrieve results on Hydrata Cloud. | `https://hydrata.com/mcp/` | 28 |
| [FernTool IP Lookup](https://www.ferntool.com) | IP lookup with VPN/Tor/datacenter flags, batch lookup, WHOIS (RDAP), DNS, reverse DNS, subnet math. | `https://www.ferntool.com/mcp` | 17 |
| [Oh My Share](https://openanthropic.com) | Publish HTML/code from your agent to openanthropic.com and get a shareable link. | `https://openanthropic.com/mcp` | 6 |
| [Caption-Pack](https://muse.ai/s/caption-pack-api-xfxt62ya0xcxlxhh) | Deterministic social-caption API: hooks, bodies, CTAs + hashtags as JSON. No LLM in the loop. | `https://caption-pack-mcp.onrender.com/mcp` | 3 |
| [Quadratic](https://www.quadratichq.com) | AI access to Quadratic spreadsheets: open files, run Python/SQL, query connected databases. | `https://mcp.quadratichq.com/mcp` | 5 |
| [Presend MCP Server](https://github.com/presendapp/presend-source) | Before an AI agent installs an npm/PyPI package: typosquat, vulnerability and existence checks. | `https://presend.pages.dev/mcp` | 40 |
| [Compute Connector](https://compute.cloudforbots.com) | Low on memory? Your bot sends heavy jobs to cloud sandboxes on your own provider keys. Flat fee. | `https://compute.cloudforbots.com/mcp` | 8 |
| [xytara MCP Executor](https://www.naxytra.com/agents) | Pay-per-call MCP tools for agents, settled with x402 (USDC on Base mainnet). No API keys. | `https://xytara-mcp-executor.onrender.com/mcp` | 17 |
| [Bring Your AI](https://bringyour.ai) | No-data MCP handoff for local Claude Code to Codex harness moves. $49 lifetime. | `https://bringyour.ai/mcp` | 7 |
| [AUTOGROK Desk](https://desk.grokaiapps.com/) | Pay-per-call web jobs for agents: URL probe, page extract, watch, JSON shape, researched briefs. | `https://desk.grokaiapps.com/mcp` | 7 |
| [Hera Fertility](https://herafertility.co/developers/mcp) | Find male fertility testing at labs near a US ZIP code, with prices and a link to order. | `https://herafertility.co/api/mcp` | 3 |
| [jsonaut](https://jsonaut.jsonaut-shaurya.workers.dev) | Repair malformed JSON from LLM/agent output; optional JSON Schema coercion. Free + x402 paid. | `https://jsonaut.jsonaut-shaurya.workers.dev/mcp` | 4 |
| [Senzing](https://senzing.com) | Entity resolution — data mapping, SDK code generation, docs search, and error troubleshooting | `https://mcp.senzing.com/mcp` | 13 |
| [npm-package-ws-has-241560546-weekly-downloads-but-sdk](https://github.com/nexus-mcp-infra/npm-package-ws-has-241560546-weekly-downloads-but-sdk) | Stateful WebSocket session registry with per-connection Shannon entropy delta tracking for schema di | `https://npm-package-ws-has-241560546-w-production.up.railway.app/mcp` | 5 |
| [Motion by Frapea](https://motion.frapea.com) | One sentence to a finished animation: your AI writes motion graphics as code and checks real frames. | `https://motion.frapea.com/mcp` | 19 |
| [Agent Rescue](https://agent-rescue.vercel.app) | Cross-session idempotency, URLs as schema-validated JSON, and a record of missing capabilities. | `https://agent-rescue.vercel.app/api/mcp` | 3 |
| [Galley Render](https://galleyrender.com) | JSON in, PDF out. Render invoices, certificates, reports and cards from a template and a payload. | `https://mcp.galleyrender.com/mcp` | 20 |
| [devstack-mcp](https://devstack-mcp.vercel.app) | Dev-registry data: npm/PyPI/Docker/VS Code packages, dep graphs, vulns, 50+ ecosystems. | `https://devstack-mcp.vercel.app/mcp` | 10 |
| [Plumbline — a trust layer for LLM answers](https://plumbline.lattice-sys.com/) | Every figure re-checked against SQL-computed facts; unsupported questions refused with the reason. | `https://plumbline.lattice-sys.com/mcp/demo` | 18 |
| [Ontario Protocol](https://ontarioprotocol.com) | Find live x402 APIs for any task (0.005 USDC, no match no charge); free x402 readiness checks. | `https://ontarioprotocol.com/mcp` | 17 |
| [GeniusFlow Evidence](https://geniusflow-federation.vercel.app) | Re-check pinned sources, package and cite. Live Federation MCP. No account. | `https://geniusflow-federation.vercel.app/api/mcp` | 9 |
| [US Code Federal Statutes](https://uscode.ecfr.io/developers) | Search and read U.S. Code statutes with legal and inline citations linking to uscode.ecfr.io. | `https://uscode.ecfr.io/mcp` | 3 |
| [CodeCraft](https://codecraft-ashy-seven.vercel.app) | Checks whether generated Minecraft Bedrock content will actually load. Nine read-only tools. | `https://codecraft-ashy-seven.vercel.app/mcp` | 9 |
| [InsideOut (Riley)](https://insideout.luthersystems.com) | Designs, prices, and deploys AWS/GCP cloud infrastructure from plain-English requirements. | `https://app.luthersystems.com/v1/insideout-mcp` | 24 |

### Weather, maps and travel

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Foresea Forecasting](https://foresea.ink) | Forecast future events and scan prediction-market edges. | `https://foresea.ink/mcp/` | 28 |
| [commutescout](https://github.com/nicglazkov/commutescout) | Live road conditions in 37 US states: incidents, closures, chain controls, cameras, wildfires. | `https://mcp.commutescout.com/mcp` | 10 |
| [FMCSA Carrier Intelligence](https://kmcto.github.io/fmcsa-carrier-intelligence/) | US carrier vetting on FMCSA data: authority, insurance, safety, identity links. Pay per call (x402) | `https://fmcsa-mcp-843680657471.us-central1.run.app/mcp` | 16 |
| [ERUX Astrology & Ephemeris Engine](https://erux.ai/developers/mcp) | Ephemeris natal & mundane charts, Vimshottari Dasha, transit horoscopes, Horas, and Vedic yogas. | `https://api.erux.ai/mcp` | 6 |
| [momentic](https://momenticmarketing.com/agent-tools) | Free SEO, GEO, and AEO audits: analyze any page or domain, AI-crawler access, agent readiness. | `https://momenticmarketing.com/mcp` | 11 |
| [easygroupflights](https://easygroupflights.com) | Group flight quotes for parties of 10 or more passengers. | `https://mcp.easygroupflights.com/mcp` | 5 |
| [iGods GEO Visibility Tool (GVT)](https://geo.igods.com) | GEO visibility tests, score trends, sitemap discovery, and domain monitoring for AI agents. | `https://mcp.geo.igods.com/mcp` | 19 |
| [Dogechain](https://dogechain.com) | Dogecoin blockchain lookups: transactions explained, addresses, blocks, fees, supply and charts. | `https://dogechain.com/mcp` | 9 |
| [Live Times Transit](https://livebustimes.org/mcp) | Read-only public transit departures, stop search, and city coverage for bus and train users. | `https://livebustimes.org/api/mcp` | 5 |
| [telecom-truth](https://github.com/fiberfinder/ff-app) | US telecom availability and intelligence by address, with FCC provenance. Fiber-first. | `https://mcp.fiberfinder.ai/mcp` | 5 |
| [Permit Verdicts](https://permit-api-production-7375.up.railway.app) | Building-permit verdicts by address, with cited records. SF, Seattle, Austin, NYC. Pay per call. | `https://permit-api-production-7375.up.railway.app/mcp` | 10 |
| [RewindMap](https://rewindmap.com/developers/) | Historical borders and dated map events with source attribution and coverage limits. | `https://rewindmap.com/mcp` | 4 |
| [sunnyspoints](https://sunnyspoints.com/mcp) | Live flight deals plus points-vs-cash math: transfer partners, valuations, per-leg verdicts. | `https://sunnyspoints-mcp.sunnyspoints.workers.dev/mcp` | 9 |
| [mcp](https://aeotool.io/mcp-agences) | Pilot AEO/GEO from Claude: bulk audits, server-side fixes via WordPress plugin, AI citations. | `https://aeotool.io/api/mcp` | 36 |
| [TOP GUN GEO-Lens](https://github.com/spacemandomains/top_gun_mcp_server) | Brand visibility auditing across LLMs, AI search, and answer engines with GEO reports and scores. | `https://top-gun-mcp-server.vercel.app/api/mcp` | 3 |
| [agent-planets](https://github.com/gtdfg6wgg8-ui/agent-planets-skill) | A galaxy where every AI agent owns a planet: claim free, terraform, build, visit, trade. | `https://planets.agentexchange.work/mcp` | 12 |
| [regimen](https://regimen-nu.vercel.app) | Tells you whether a trading strategy's edge is distinguishable from luck. | `https://regimen-nu.vercel.app/mcp` | 4 |
| [KlearFlow Relay](https://github.com/erickmckee/klearflow) | Machine-paid revenue intelligence, recovery decisions, and x402 routing for AI agents. | `https://klearflow.vercel.app/mcp` | 3 |
| [Singapore Event Print & Merch Quotes](https://quote-mcp.galvanized-purchase.workers.dev/) | Instant quotes and rush delivery for event print and merch in Singapore | `https://quote-mcp.galvanized-purchase.workers.dev/mcp` | 11 |
| [Veabird: ski & beach trip planner](https://veabird.com/ai/) | Ski & beach trip planning: resort matching, snow and sargassum forecasts, lodging and flights. | `https://veabird.com/mcp` | 16 |
| [Your Travel Radar](https://yourtravelradar.com) | Dated, sourced facts on European night train stations and lines, and measured punctuality. | `https://yourtravelradar.com/mcp` | 7 |
| [MapPoster](https://mapposter.xyz) | Design map posters of any place in 50+ styles, with names, dates and markers, and order prints. | `https://mcp.mapposter.xyz/mcp` | 3 |
| [HORIZON SHIELD: Construction Estimate Auditor for Japan (KIRA)](https://shield.the-horizons-innovation.com) | Agent intake desk for property renovation. Read only, CORS open, fail closed, receipts recompute. | `https://web.horizonshield.dev/mcp` | 5 |
| [AirTreks MCP](https://airtreks.com) | Multi-city flight routing intelligence — plan RTW trips, validate alliances, get carrier picks. | `https://mcp.airtreks.com/mcp` | 11 |
| [2027 連假與訂票](https://tw-travel-2027.panda198271.workers.dev) | 2027 台灣連假、出國目的地擁擠度與機票訂票時機建議。 | `https://tw-travel-2027.panda198271.workers.dev/mcp` | 5 |

### Media and content

| Server | What it does | URL | Tools |
|---|---|---|---|
| [maginary-mcp](https://maginary.ai/mcp) | AI image + video generation for agents: --flag prompt DSL, async generate/poll, x402 pay-per-use. | `https://mcp.maginary.ai/mcp` | 16 |
| [Starcovery](https://www.starcovery.com) | MCP tools to find and hire Instagram and TikTok creators from a plain-language brief. | `https://www.starcovery.com/api/mcp` | 28 |
| [EasyGerber: AI PCB design, layout, and routing](https://www.easygerber.com/agents) | AI PCB design, layout, and routing | `https://www.easygerber.com/api/mcp` | 17 |
| [agents](https://vevang.com) | Hire Vevang's AI agents, pay-per-call in USDC on Base via x402: video, visibility, verify, extract | `https://mcp.vevang.com/mcp` | 6 |
| [Guest Pictures](https://guest-pictures.com) | Free browser photo booth with effect picker, plus info on collecting guest photos via QR code. | `https://guest-pictures.com/mcp` | 3 |
| [Starchild Music](https://starchild.music/app) | Find and license original songs to record. Hear every song in many production styles. | `https://mcp.starchild.music/mcp` | 11 |
| [Motion Menu](https://www.motionmenu.ca) | 597 motion/3D UI patterns as ready HTML/CSS/JS, served over MCP. The entire library is free. | `https://www.motionmenu.ca/api/mcp` | 11 |
| [InstaVeil Agent Commerce](https://instaveil.com/agent-commerce) | Instagram research, Story monitoring and creator comparison. MCP x402 paid calls, USDC on Solana. | `https://instaveil.com/mcp` | 7 |
| [Chart Color System](https://socraticstatic.github.io/Visualizations/mcp-docs.html) | Solve, audit and simulate colorblind-safe chart palettes. WCAG contrast, OKLab ΔE. Read-only. | `https://chart-color-mcp.vercel.app/mcp` | 4 |
| [AXIS Avatar Foundry](https://avatar.jonathanarvay.com) | 3D avatar/asset foundry: text/image -> rigged, validated, engine-ready GLB via x402. | `https://api.avatar.jonathanarvay.com/mcp` | 14 |
| [GrowVib: Social Media Growth](https://growvib.com/mcp) | Discover, compare and buy social media growth for Instagram, TikTok, YouTube, Telegram, X and more | `https://api.growvib.com/mcp-public` | 9 |
| [Tonebook Palette](https://tonebook.app) | Choose a palette, compare digital colors and create portable outfit, event or packing boards. | `https://tonebook-muse-mcp-staging.vercel.app/api/openai-mcp-v1` | 6 |
| [Sleek](https://sleek.design/agents) | Design your mobile app UI with AI, then have your coding agent build the real app from it. | `https://sleek.design/api/mcp` | 12 |
| [SlotMaps](https://slotmaps.com/connect) | Advantage-play guides for 360+ casino slot machines: what to look for and when one is worth playing. | `https://slotmaps.com/mcp` | 5 |
| [SafeResize](https://saferesize.com/ai) | Passport and visa photo rules for 110 documents in 60 countries, and upload limits as exact numbers. | `https://saferesize.com/mcp` | 4 |
| [Lacuna Music](https://www.lacuna.fm) | Generate AI music via the Lacuna Music API from MCP clients like Claude Desktop & Code. | `https://www.lacuna.fm/mcp` | 3 |
| [FounderBrain](https://thinkreasonlearn.com/founderbrain) | See how a founder came across in a pitch or investor call, compared with 773 founder interviews. | `https://mcp.thinkreasonlearn.com/mcp` | 3 |
| [GiftsToPrint](https://mcp.giftstoprint.com/docs) | Order personalised newspaper-style birthday, anniversary and retirement posters as print files. | `https://mcp.giftstoprint.com/mcp` | 5 |
| [Craftery Developer Tools](https://craftery.dev/mcp) | Developer utilities: color conversion, WCAG contrast, timestamps, UUIDs, and hashing. | `https://craftery.dev/mcp` | 6 |
| [Postclick by PPC.io: Landing Page CRO](https://ppc.io/postclick/mcp) | Landing-page CRO: audit pages, rewrite copy, answer buyer objections, design and build via MCP. | `https://mcp.ppc.io` | 21 |
| [Vision Driven Design (VDD) MCP Server](https://vdd.simonmak.com) | Spec-driven development MCP server: 8 phases, bi-directional traceability, 7 quality gates. | `https://vdd.simonmak.com/api/mcp` | 15 |
| [The Scribble Thing](https://scribble.boringstuff.club) | Turn one line-art image into a prompt-directed, hand-drawn scribe animation MP4. | `https://scribble.boringstuff.club/mcp` | 6 |
| [kavel-mcp](https://www.kavel.ai) | Discover Kavel's AI photo/video generators, get tuned prompts, and open the right tool on kavel.ai. | `https://www.kavel.ai/api/mcp` | 4 |
| [social-data](https://honesthook.com) | Instagram, TikTok, Threads, Bluesky and 8 more: one API, one key, one JSON shape | `https://honesthook.com/api/mcp` | 12 |
| [OffStereo](https://www.offstereo.com/chatgpt) | Builds narrated, playable music stories, explores sample lineage, and saves verified playlists. | `https://www.offstereo.com/api/mcp` | 12 |

### Finance and crypto

| Server | What it does | URL | Tools |
|---|---|---|---|
| [giteasy](https://github.com/greenmtnsun/GitEasy-internal) | Plain-English git via MCP: 22 tools to branch, commit, push, and tag. No git jargon. | `https://giteasy-mcp.azurewebsites.net/mcp` | 22 |
| [Senaro Personal Finance](https://senaro.ai) | Credit card payoff, mortgages, refinancing, 401(k), rent vs buy. Every rule and default is cited. | `https://mcp.senaro.ai/mcp` | 18 |
| [Readout](https://readout-7pt.pages.dev) | Measured readings on open-source dependencies: health, end-of-life, model prices, incidents. | `https://readout-7pt.pages.dev/api/mcp` | 31 |
| [agenticfeed](https://agenticfeed.ai) | Match shopper intent to a merchant's products and fetch live price, stock and product Q&A. | `https://agenticfeed.ai/mcp` | 4 |
| [invinoveritas](https://github.com/babyblueviper1/invinoveritas-mcp) | Second opinion before an irreversible agent action; signed proofs, free verify, public ledger. | `https://api.babyblueviper.com/mcp/verify` | 10 |
| [AI2Fin (2Fin) Tax MCP](https://github.com/embracingearth-space/ai2fin-tax-mcp) | Free public tax MCP: GST/VAT, income, company & capital-gains tax for 50+ countries, source-cited. | `https://taxmcp.ai2fin.com` | 10 |
| [x402-seller — rug protection & safe-alpha for trading agents](https://github.com/wyattpalm2-eng/x402-seller) | Rug-check & launch radar for trading agents: composite honeypot score, EVM+Solana, keyless x402. | `https://x402-seller-m8nx.onrender.com/mcp` | 7 |
| [Solana Pulse: agent safety layer](https://solana-pulse-gateway-1021990235790.us-central1.run.app/docs/) | Stops AI agents losing money on Solana: pre-sign checks, intent matching, token verdicts. x402 USDC. | `https://solana-pulse-gateway-1021990235790.us-central1.run.app/mcp` | 15 |
| [FURRINGLINE](https://mcp.furringline.com/docs) | Thai building materials: product search, prices before VAT, stock and material calculators. | `https://mcp.furringline.com` | 5 |
| [MetaLend](https://mcp.metalend.tech/docs/) | Browse, deposit, withdraw & rebalance stablecoins on Aave, Morpho & Euler across major EVM chains. | `https://mcp.metalend.tech/mcp` | 19 |
| [Kristo Intelligence](https://kristo-intelligence-api.onrender.com) | Pay-per-call DeFi intelligence for AI agents on Base — x402, USDC, no keys. | `https://kristo-intelligence-api.onrender.com/mcp` | 3 |
| [mcp-x402 — MCP server for agents with autonomous USDC/RLUSD payments](https://github.com/timwal78/SML_Portfolio) | 85+ pay-per-call MCP tools: trading, federal grants/contracts, SEC, FTD. x402 USDC/RLUSD. No keys. | `https://mcp-x402.onrender.com/mcp` | 3 |
| [SweKit - Swedish validators](https://swekit-api.zenith-ops.workers.dev/docs) | Swedish personnummer/orgnr/bankgiro/OCR validation, kontonummer to IBAN, bankdagar. | `https://swekit-api.zenith-ops.workers.dev/mcp` | 13 |
| [Agent Arena](https://github.com/agentarenaleague/agent-arena) | Paper trading only. 26 leagues for AI bots. Spot Crypto + Crypto 35 live. Register by MCP. | `https://agentarenaleague.pages.dev/mcp` | 31 |
| [verantis-mcp](https://github.com/m9labs-railscope/verantis-mcp) | Verified directory for machine payments (x402 & MPP): check services and wallets before agents pay. | `https://api.verantis.ai/mcp` | 4 |
| [Espresso Steals](https://espressosteals.com/for-agents) | Espresso gear price history: live Amazon prices, 2+ years of daily data, BUY calls at verified lows. | `https://espressosteals.com/api/mcp` | 4 |
| [GolfPrice AI](https://golfpriceai.com/ai.html) | Live UK golf equipment prices, price history and genuine price drops from GolfPrice AI. | `https://golfpriceai-mcp.golfpriceai.workers.dev/mcp` | 5 |
| [Paw Pulse](https://pawpulse.dougalpaw.workers.dev) | Heartbeat and tokens/sec monitoring for self-hosted LLM servers (Ollama etc.), with down alerts. | `https://pawpulse.dougalpaw.workers.dev/mcp` | 6 |
| [Tokenbooks - crypto and fiat accounting and payments](https://tokenbooks.io/use-cases/ai-accounting) | Crypto and fiat on one double-entry ledger: sync wallets, reconcile, cost basis, audit-ready close. | `https://api.tokenbooks.io/mcp` | 36 |
| [mcp](https://birkinbagstock.com) | Live Hermes Birkin & Kelly market data: resale inventory, prices, auction calendar and results | `https://birkinbagstock.com/mcp` | 14 |
| [cryptofeed402](https://cryptofeed402.site) | Crypto market data for AI agents: Hyperliquid funding/OI, OKX spot, twice-daily brief. x402 USDC. | `https://cryptofeed402.site/mcp` | 9 |
| [Tideline Money Tools](https://mcp.tideline.money/) | Free money calculators: option expiry risk, debt avalanche, cash runway, subscriptions, invoices. | `https://mcp.tideline.money/mcp` | 7 |
| [Fantasize cruise finder](https://fantasize.net/llms.txt) | Find the best-value cruise: 23 lines, ~30k sailings priced nightly, low/high vs usual, book link. | `https://fantasize.net/mcp` | 10 |
| [Mansa African Markets](https://mansamarkets.com) | Live African stock market data — NGX, GSE, NSE, JSE, BRVM and 8 more. Prices, indices and movers. | `https://mcp.mansamarkets.com/mcp` | 21 |
| [JustIdea Agency](https://justidea.agency/) | Services, prices, inquiries and free analytics, AI and Google visibility scans by JustIdea, Poland. | `https://justidea.agency/mcp` | 8 |

### Science, health and research

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Appeal My Claim](https://goodturn-mcp.pages.dev/appealmyclaim) | Appeal a denied US health insurance claim: denial codes, rights, deadlines and a draft letter. | `https://goodturn-mcp.pages.dev/appealmyclaim/mcp` | 4 |
| [research-intel](https://research.dropwatchhq.com) | Research GTM triggers: new NIH grants by PI/institution and new clinical trials by sponsor/phase. | `https://research.dropwatchhq.com/mcp` | 5 |
| [SDSentry — SDS Lookup & OSHA HazCom](https://sdsentry.0xpi.com) | Free SDS lookup for one product or a whole chemical inventory list, plus a HazCom readiness check. | `https://sdsentry.0xpi.com/mcp-sds` | 3 |
| [quorum](https://github.com/Godzilla-lab/Quorum-API) | Market evidence with receipts: every claim resolves to a real stored record you can fetch back. | `https://quorum-api-j15n.onrender.com/mcp` | 5 |
| [dynamic-health-monitor](https://health.getvda.ai) | Give it one seed; it finds every service and checks HTTP, TCP, SSL and DNS. | `https://health.getvda.ai/mcp` | 5 |
| [Prediction Market X Sentiment](https://prediction-bot-iggf.onrender.com/about) | Polymarket & Kalshi sentiment from X (Twitter) via Grok. Free daily scores; live scoring via x402. | `https://prediction-bot-iggf.onrender.com/mcp` | 9 |
| [healthcovered-mcp](https://github.com/hillsidecoastal-glitch/healthcovered-mcp) | ACA health insurance eligibility, subsidy checker, and enrollment dates for 2026. | `https://healthcovered-mcp.onrender.com/mcp` | 3 |
| [Taco Street Locating](https://ai.tacostreetlocating.com) | Free human-backed apartment locating for Austin, Dallas & Houston, TX. A free locator books tours. | `https://ai.tacostreetlocating.com/mcp` | 9 |
| [knos](https://github.com/drexthealpha/Knos) | The neutral meter for AI agent work: neither side keeps the count. | `https://knos.onrender.com/mcp` | 29 |
| [TickerFacts](https://tickerfacts.com/developers) | SEC EDGAR fundamentals as agent tools: look up or screen US public companies. Free, no key, CC0. | `https://tickerfacts.com/mcp` | 10 |
| [draconic21 Daily Agent Signal + x402 Data Tools](https://draconic21-x402-api.onrender.com/llms.txt) | Daily Agent Signal: x402 research; coverage varies. Free preview, $0.03 USDC on Base. SEC/OFAC. | `https://draconic21-x402-api.onrender.com/mcp/free` | 30 |
| [intelligence](https://edge-agents.ai/agents/mcp) | Macro, market and decision intelligence over x402. Gaps are unavailable rather than estimated. | `https://pay.edge-agents.ai/mcp` | 7 |
| [Mara Briefing Service](https://mara-briefings.onrender.com) | Paid research briefings for agents: $0.10 USDC/question on Base Sepolia via x402. ERC-8004 #9395. | `https://mara-briefings.onrender.com/mcp` | 5 |
| [mcp](https://rxmanager.ai) | Live US drug acquisition costs (CMS NADAC) for AI assistants. Free, no auth, weekly data. | `https://mcp.rxmanager.ai/mcp` | 8 |
| [FinchNode Synthetic Health Records](https://finchnode.com/developers/demo-api) | Synthetic EHR: medications, labs, conditions, allergies, immunizations, FHIR R4. No API key. | `https://api.finchnode.com/demo/mcp` | 14 |
| [Lowtoxgear Scanner](https://github.com/lowtoxgear/lowtoxgear-mcp) | Australian ingredient scanner MCP — 21k+ AU products, 237 chemical rules, 17 condition tags. | `https://mcp-scan.lowtoxgear.com/mcp` | 5 |
| [x402 Micropayments MCP](https://x402-mcp.onrender.com) | Pay-per-call US city property compliance and Base tx checks, paid in USDC on Base via x402. | `https://x402-mcp.onrender.com/mcp/mcp` | 20 |
| [CutGPT Research & Fact-Check](https://cutgpt.app/mcp/) | Free fact-checks, papers, source vetting, plus verified AI pricing, comparisons, guides, and tools. | `https://mcp.cutgpt.app/mcp` | 14 |
| [Emora Health](https://www.emorahealth.com) | Find kids' and teens' mental health clinicians, check availability, get booking links and costs. | `https://www.emorahealth.com/api/mcp/v1` | 8 |
| [Zicron medical chronology (public)](https://claims.zicron.ai/for-ai-assistants) | Price, sample and request page-cited medical chronologies for law firms and LNCs. No sign-in or PHI. | `https://claims.zicron.ai/mcp` | 5 |
| [Hedge Fund Alpha Research](https://hedgefundalpha.com/mcp-docs) | Search public Hedge Fund Alpha metadata and find official membership and data product pages. | `https://hedgefundalpha.com/mcp` | 7 |
| [CrashStory MCP](https://crashstory.com/mcp) | Colorado personal injury attorney directory, AI-analyzed review intelligence, and crash data | `https://crashstory-mcp-production.up.railway.app/mcp` | 18 |
| [Medicare Enrollment and Revalidation Data](https://actablesite.com/medicare-revalidation-mcp-server) | Free CMS enrollment and revalidation evidence with pay-per-result automation and Roster Watch terms. | `https://actablesite.com/mcp/pending-medicare/` | 4 |
| [RoboParts 机器人零部件兼容性](https://roboparts.cc) | 852 humanoid/bionic robot parts, 20 categories, 4-dimension compatibility checking. Vendor-neutral. | `https://roboparts.cc/mcp` | 20 |
| [Gridzen Verification](https://gridzen.ai/developers/) | Country verification research, integration planning and synthetic tests. No live identity checks. | `https://gridzen.ai/developers/mcp` | 5 |

### Open data and government

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Intelligence Aeternum](https://iaeternum.ai) | AI training dataset marketplace: 2M+ museum artworks with Golden Codex enrichment | `https://fluora-mcp-172867820131.us-west1.run.app/mcp` | 3 |
| [StackData](https://stackdata.io) | Official statistics, China censuses & yearbooks, and as-of customs tariffs with legal citations. | `https://api.stackdata.io/mcp` | 6 |
| [Money Mind — the judge](https://money-mind-extract.onrender.com/integrate) | Statistical adjudication for agents: backtest judges, fact-checks. Pay per call in USDC via x402. | `https://money-mind-extract.onrender.com/mcp` | 17 |
| [European IP Data & Analytics — IPRATE](https://iprate.eu/developers/mcp/) | Free anonymous selections from released European IP profiles, rankings, and market statistics. | `https://mcp.iprate.eu/mcp` | 6 |
| [Sovereign AI Act MCP](https://www.regulatoryai.eu/mcp/) | Classify any AI system under the EU AI Act: risk tier + binding Articles, verbatim from the law. | `https://www.regulatoryai.eu/mcp` | 5 |
| [Australian Economic Data (ABS, RBA & APRA)](https://github.com/AnthonyPuggs/ausecon-mcp-server) | Australian economic data from the ABS, RBA, and APRA: CPI, GDP, cash rate, labour, and more. | `https://mcp.auseconmcp.com/mcp` | 14 |
| [Fromerica U.S. Trade Data](https://www.fromerica.com/developers#mcp) | U.S. tariffs (HTS), Schedule B codes, export statistics, party screening and FMC license checks. | `https://api.fromerica.com/mcp` | 8 |
| [Launch529: 529 plans and college costs](https://launch529.com/connect) | Compare state 529 plans, look up college costs and check qualified 529 expenses. Free, no key. | `https://launch529.com/api/public/mcp` | 7 |
| [Agent Observatory](https://agent-observatory-flame.vercel.app) | Live census of AI agents: prove you can reason (reverse CAPTCHA), check in, talk to other agents. | `https://agent-observatory-flame.vercel.app/api/mcp` | 6 |
| [SAASH Saudi Government, Business, Workforce & Legal Services \| خدمات سعودية للوكلاء](https://saash-gateway.vercel.app) | Saudi government, citizen, business, legal and workforce service discovery in Arabic and English. | `https://saash-gateway.vercel.app/mcp` | 4 |
| [CRE Intelligence](https://cre-intelligence-mcp.vercel.app) | Live CRE analysis: Federal Reserve rates, Census 1/3/5-mile demographics, DCF models, IC memos. | `https://cre-intelligence-mcp.onrender.com/mcp` | 13 |
| [Legal HQ: Legal AI Help for Lawsuits](https://legalheadquarters.com) | Legal AI help for business lawsuits: organize your case with AI and cut legal fees. Not a law firm. | `https://legalheadquarters.com/mcp` | 4 |
| [chesswithclaw](https://github.com/Alightttt/ChessWithClaw) | Play chess live against your own personal AI agent — OpenClaw, Hermes, and similar. | `https://chesswithclaw.vercel.app/api/mcp` | 14 |
| [China Visa & Regulation Data](https://cnregwatch.com) | China visa-free eligibility by nationality and latest official regulation changes, with sources. | `https://cnregwatch.com/mcp` | 5 |
| [vigo-mcp](https://github.com/OrphicOne-Platform/vigo-mcp) | AI-powered Hong Kong SFC regulatory intelligence. Bilingual EN/ZH compliance queries. | `https://lsoatzzwpltpydwyfqqv.supabase.co/functions/v1/vigo-mcp` | 10 |
| [Corpus Law](https://corpuslaw.us/docs/mcp) | Search and cite US law from official sources, then form an LLC or nonprofit with free agent tools. | `https://corpuslaw.us/api/mcp` | 10 |
| [Al-Taswia Iraqi Law Research](https://www.al-taswia.com) | Read-only search of Al-Taswia's published Iraqi law articles. General information, not legal advice. | `https://al-taswia-iraqi-law-research.al-taswia.workers.dev/mcp` | 3 |
| [Lipe Court Record](https://lipe-api-production.up.railway.app/connect) | Search page-cited evidence from the public court record in Lipe v. Lupus Superior. | `https://lipe-api-production.up.railway.app/mcp` | 7 |
| [HumanFn](https://humanfn.com/agents) | Qualified human outcomes for AI agents: attorney review of SaaS Terms/Privacy, on-site checks. | `https://humanfn.com/mcp` | 9 |
| [Rettsarkiv](https://rettsarkiv.no) | Norske Høyesterettsavgjørelser og lovtekst som lov-bevisst data, søkbart på vanlig norsk. | `https://rettsarkiv-mcp-953525390683.europe-west3.run.app/mcp` | 8 |
| [Prop Firm Discount MCP](https://propfirmdiscount.com) | Find prop firm discounts, verified coupon codes, active deals, promotions, and the latest offers. | `https://mcp.propfirmdiscount.com/mcp` | 8 |
| [California Court Deadlines](https://calcourtdeadlines.com) | Computes California state court deadlines and cites the code section behind every date. No API key. | `https://calcourtdeadlines.com/api/mcp` | 9 |
| [ADF: EU Tenders, EU Funding, EU Medicines, CVE KEV EPSS, EU CERT Advisories, Amsterdam Events](https://agentdatafeed.com) | EU tenders, funding and medicines, CVEs with KEV and EPSS, EU CERT advisories, Amsterdam events. | `https://agentdatafeed.com/mcp` | 3 |
| [Spatial India](https://spatialindia.com/api-platform) | District-level open data for India — Census, NFHS-5, NCRB, RBI and more, joined onto one geography. | `https://api.spatialindia.com/mcp` | 6 |
| [Infinivo AI Front Desk](https://infinivoai.eu/mcp) | Run a live AI intake desk for personal-injury law firms, or query pricing, proof and positioning. | `https://infinivoai.eu/mcp` | 10 |

### Business and marketing

| Server | What it does | URL | Tools |
|---|---|---|---|
| [購物比價紀錄](https://shop.penguindriver.com) | 購物比價紀錄：3C、美妝、家電價格比較。台灣繁體中文 MCP 工具。 | `https://shop.penguindriver.com/mcp` | 7 |
| [Verity](https://github.com/veritylabsai/verity) | Cited product-compliance ground truth for AI agents. Never generates; always cites. | `https://verity-mcp-243195959173.us-central1.run.app/mcp` | 4 |
| [HireLocksmiths — Locksmith Finder](https://hirelocksmiths.com) | Find a vetted U.S. locksmith, request a quote or booking; products for locksmith businesses. | `https://hirelocksmiths-mcp.onrender.com/mcp` | 7 |
| [namemyapp](https://namemy.app/agents) | Brandable business names with live domain availability + one-click buy URLs. | `https://mcp.namemy.app/direct` | 13 |
| [搜尋引擎與 AI 爬蟲工具箱](https://tw-search-seo.panda198271.workers.dev) | 檢查網站爬蟲設定、驗證爬蟲 IP、IndexNow 提交與 YouTube SEO 檢查。 | `https://tw-search-seo.panda198271.workers.dev/mcp` | 14 |
| [VeritaHire Hiring Intelligence](https://veritahire.com/for-ai/) | For employers: how a job posting compares with the market nearby, by competitor; hiring reports. | `https://veritahire.com/mcp/employers` | 4 |
| [WebZum - Websites for Small & Local Businesses](https://webzum.com) | Describe a local business, verify the owner email: SEO site, hosting, chatbot, Google Ads. | `https://webzum.com/api/mcp` | 6 |
| [lead-stampede](https://github.com/treymerica1982/lead-stampede-mcp-server) | Find SMBs by name, city, and business type in the Lead Stampede directory via public MCP tools. | `https://lead-stampede-mcp-server-production.up.railway.app/mcp` | 13 |
| [ai-commerce](https://airy-enthusiasm-production.up.railway.app) | The first marketplace where AIs buy from AIs. Browse, register, and purchase autonomously. | `https://airy-enthusiasm-production.up.railway.app/mcp` | 6 |
| [Fleek for Business](https://www.getfleek.app) | Subscription brands a card, loyalty, benefits or telco programme could offer, by market. | `https://mcp.getfleek.app/registry/mcp` | 6 |
| [FORGE compliance and business decision tools](https://forge-engine-production-58cc.up.railway.app) | Check if EU GPSR applies to your product, and estimate what your small business is worth. | `https://forge-engine-production-58cc.up.railway.app/mcp` | 8 |
| [glassypic](https://github.com/onepunchtechnology/glassypic-mcp-server) | Production-ready images in one pass: resize, crop, compress, convert format, upscale, tag for SEO | `https://app.glassypic.com/mcp` | 3 |
| [pops4-mcp-catalog](https://huanggoodman.com) | AI-native corporate gifting & event infrastructure for Fortune 500. 70K products, 200+ brands. | `https://mcp.pops4.com/mcp` | 13 |
| [Bizfile MCP](https://kordagencies.com) | Company intelligence via UK Companies House and risk screening across 386 risk data sources. | `https://bizfile-mcp-production.up.railway.app` | 3 |
| [Scout Packs](https://github.com/tigerops-win/scout-packs) | B2B data for AI agents: lead lookup, deliverability scoring, domain intel. x402 $0.01-$0.03/call. | `https://scout-packs-production.up.railway.app/mcp` | 16 |
| [Atlas Data Exchange](https://app.atlasipholdingsllc.com/intelligence?src=mcp_registry) | Infrastructure and hazard intelligence with provenance, spatial confidence and quality contracts. | `https://app.atlasipholdingsllc.com/mcp?src=mcp_registry` | 10 |
| [jp-biz-opportunity](https://github.com/kodandy/jp-biz-opportunity-mcp) | Japanese public-sector business opportunities for AI agents: tenders, subsidies, sanctions. x402. | `https://jp-biz-opportunity-62ko7b2uwa-an.a.run.app/mcp` | 6 |
| [MaterialHandling.com](https://materialhandling.com/mcp) | Industrial equipment catalog: 15,000+ products, specs, live LTL freight rates, real quote requests. | `https://materialhandling-7c6.pages.dev/mcp` | 5 |
| [Realask - verified answers from the physical world](https://realask.net) | Ask a US local business a current question by phone. Typed, timestamped answers for agents; x402. | `https://realask.net/mcp` | 5 |
| [OpenFab](https://github.com/yyphilo/openfab) | Instant parametric cost estimates for custom manufacturing: CNC, molding, sheet metal, 3DP, PCB. | `https://openfab-22100483453.us-central1.run.app/mcp/` | 7 |
| [mcp](https://www.sitepulsar.ai) | SitePulsar AEO audits: fetch FIND/READ/USE agent-readiness scores for any website. | `https://mcp.sitepulsar.ai/mcp` | 13 |
| [Instilus small-business decision tools](https://www.instilus.com) | Valuation, EBITDA, break-even, margin, rates, acquisition, competitor research, store audit. | `https://www.instilus.com/mcp/v1` | 8 |
| [catalog](https://nontoxicnook.com/connect) | Read-only tools over an independently vetted catalog of non-toxic home and baby products. | `https://api.nontoxicnook.com/api/mcp` | 7 |
| [pocket-agent-mcp](https://aipocketagent.com/docs) | Pocket Agent (aipocketagent.com) MCP server — read tools for personas, apps, and product info. | `https://aipocketagent.com/api/mcp` | 4 |
| [Pay Transparency Rules for Job Posts](https://pay-transparency-rules.nerolabs.workers.dev/) | Must a job post show pay? Rules for US states and cities, Canada and all 27 EU countries. Sourced. | `https://pay-transparency-rules.nerolabs.workers.dev/mcp` | 4 |

### AI, agents and memory

| Server | What it does | URL | Tools |
|---|---|---|---|
| [agentstack-mcp](https://github.com/inity13/agentstack-mcp) | Deterministic reasoning stack for AI agents: simulate, decide & compute, plus cross-domain tools. | `https://agentstack-mcp.pages.dev/mcp` | 24 |
| [CanaryGuard 402](https://canaryguard-402.onrender.com) | Deterministic prompt-injection detection & sanitization for AI agents via x402 on Base. | `https://canaryguard-402.onrender.com/mcp` | 34 |
| [fixflow](https://github.com/MagneticDogSon/fixflow-mcp) | Collective memory for AI agents. One agent solves a bug — every agent gets the fix instantly. | `https://fixflow-mcp.onrender.com/mcp` | 3 |
| [RFix](https://rfix.ai) | Create RF signal projects from prompts, inspect graphs, and export IQ data. | `https://mcp.rfix.ai/mcp` | 6 |
| [designforyou](https://designforyou.swapp1990.org) | Generate logos, social posts, app screenshots, comic panels & visual-novel assets from prompts. | `https://designforyou.swapp1990.org/mcp/v2/` | 14 |
| [el-buen-agente-mcp](https://github.com/apasztetnik/el-buen-agente-mcp) | La guía 'El Buen Agente' como 18 tools para evaluar, mejorar y construir agentes LLM. En español. | `https://el-buen-agente-mcp-production.up.railway.app/mcp` | 18 |
| [Gemot Deliberation Server](https://gemot.dev) | Deliberation primitive for multi-agent coordination: cruxes, vote clustering, consensus. | `https://gemot.dev/mcp` | 7 |
| [ChangePacket](https://cibcxqrqiqvzpardbdrw.supabase.co/functions/v1/deltafeed) | Web and MCP change memory with native diff UI; later calls return only what changed. | `https://cibcxqrqiqvzpardbdrw.supabase.co/functions/v1/changepacket-mcp` | 3 |
| [ActableSite AI Crawler Monitor](https://actablesite.com/mcp-server) | Check AI crawler robots.txt policy and monitor public-site policy, sitemap, and llms.txt changes. | `https://actablesite.com/mcp/` | 5 |
| [OmniProvider](https://provider.omnidev.tech) | Pay-per-call LLM API for agents: model catalog, pricing, unpaid x402/MPP quotes, how-to-pay. | `https://mcp.omnidev.tech/mcp` | 4 |
| [events](https://urbanplayground.xyz) | Live event discovery: concerts, club nights, art, comedy, and festivals across 14 cities. | `https://eventchat-events-mcp-production.up.railway.app/mcp` | 30 |
| [memxus](https://github.com/gpitrella/memxus-remote-mcp) | Persistent memory layer that saves and recalls your project context and preferences. | `https://mcp.memxus.com/mcp` | 9 |
| [Proofsource](https://proofsource.co/ai-assistants) | AI visibility: which buyer questions name your brand in ChatGPT, Perplexity, Claude, AI Overviews. | `https://app.proofsource.co/v1/mcp` | 14 |
| [Agentic Prompt](https://github.com/KunaniGaming/agentic-prompt) | 1,177 free agentic trading prompts for Claude and Robinhood MCP. | `https://agentic-prompt.com/mcp` | 4 |
| [Model Tested](https://modeltested.com/mcp/) | Independent test scores for open-weight LLMs: best model for your GPU or Mac, comparisons. | `https://modeltested.com/mcp` | 5 |
| [No-Shell Agent Architect MCP](https://github.com/loved0543-dotcom/no-shell-agent-operating-pack) | Turns vague automation requests into tool stacks, prompts, QA checks, and human boundaries. | `https://ai-automation-operating-pack.vercel.app/api/mcp` | 7 |
| [Cortex](https://skynetlab-cortex.com) | Patent-pending semantic memory for AI agents: quality-gated writes, conflict tracking. Free trial. | `https://skynetlab-cortex-saas-mcp.cortex-320.workers.dev/mcp` | 7 |
| [Markdown Lane Check - llms.txt, .md twins, Accept: text/markdown](https://www.pathwren.workers.dev/c/mcp-registry-official/mcp-markdown.html) | Six checks: llms.txt, llms-full.txt, .md twins, Accept: text/markdown, sitemap.md, alt link. Free. | `https://www.pathwren.workers.dev/c/mcp-registry-official/mcp/markdown` | 5 |
| [agent-ready-kit](https://mudko.com) | Agent-readiness scanner (0-5 score), robots.txt + llms.txt generators, managed agent enablement. | `https://mudko.com/api/mcp` | 26 |
| [rtcf](https://rtcf.happlen.com) | Turns rough requests into sharp Role/Task/Context/Format prompts. Thai and English. | `https://rtcf.happlen.com/api/mcp` | 3 |
| [TestGraph](https://github.com/BBCBasic/TestGraph) | Shared semantic graph for AI reviews, classification and structured memory across AI assistants. | `https://testgraph.21dle.co.uk/mcp-v2` | 37 |
| [Continuity by Ouroboros Apps](https://continuitywriter.com) | Story continuity, novel memory, and series bible for fiction writers, shared with AI assistants | `https://continuitywriter.com/mcp` | 11 |
| [KitRank use cases](https://kitrank.dev/mcp.html) | Read-only catalog of 660 real, sourced AI agent use cases with tools, cost and setup prompts. | `https://kitrank.dev/api/mcp` | 5 |
| [quorum](https://github.com/terradev-cloud/quorum-mcp) | Attested multi-agent consensus: proposals, votes, and outcomes stamped and traced. | `https://quorum-mcp.terradev.cloud/mcp` | 7 |
| [CatchUI](https://catchui.com/mcp) | What is this UI element called? 50 curated UI patterns, names per platform, build prompts. EN/中文. | `https://catchui.com/api/mcp` | 6 |

### Utilities

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Navigi: community services across Canada](https://navigi.ca) | Community services in every Canadian community, each with the date it was last checked. | `https://api.navigi.ca/v1/mcp` | 4 |
| [The Automators](https://theautomators.ai/mcp/) | Read-only MCP server for The Automators: services, pricing, industries, case studies, calculators. | `https://mcp.theautomators.ai/mcp` | 18 |
| [tools](https://fluentedi.com) | 49 free agent tools: WHOIS, PDF to text, email checks, FX rates, X12 EDI, JSON repair. No API key. | `https://fluentedi.com/mcp` | 19 |
| [Commonlands Optics: M12 Lens and C-Mount Lens Finder + Field-of-View Calculator](https://commonlands.com/pages/agentic-mcp-for-m12-lenses-and-optics) | M12 lens and C-mount lens finder with image-sensor matching and field-of-view calculator. | `https://mcp.commonlands.com/mcp` | 21 |
| [HiveGate](https://www.hiveagentiq.com) | Agent admission queue with capacity control and priority tiers | `https://hivegate.onrender.com/mcp` | 4 |
| [secondstrike](https://secondstrike.io/skill.md) | Command a nation in SECOND STRIKE, a real-time war game. Join a war, give orders, climb the ladder. | `https://secondstrike-server-zgqvqzdrta-uc.a.run.app/mcp` | 10 |
| [UK Legislation Changes](https://uk-legal-changes.pages.dev) | Point-in-time amendment history for 506 UK legislation provisions. | `https://uk-legal-changes.pages.dev/mcp` | 4 |
| [Prince Cloud](https://prince.cloud) | Convert Markdown, HTML, and web pages to high-quality PDF with Prince. | `https://prince.cloud/mcp` | 3 |
| [OKC HVAC Calculator \| Repair or Replace Decision Tool](https://okchvaccalculator.com) | Use the free OKC HVAC Calculator to see whether repairing or replacing your heating or air system ma | `https://okchvaccalculator.com/mcp` | 8 |
| [utility-converter](https://github.com/punchfan01/utility-converter) | 7 utility tools in here: exchange rate, UUID, hash, Base64, timestamp, calculator, unit conversion. | `https://utility-converter.onrender.com/mcp` | 7 |
| [x402 Web Tools](https://github.com/iparadise71/x402-api) | Pay-per-call tools for agents: web page to Markdown, tech stack, email domain check (x402 USDC) | `https://x402-web-tools.onrender.com/mcp` | 4 |
| [Calendar Agent by Nova (CIVAI)](https://nova.civai.co/agent/calendar-agent) | I do everything related to calendar scheduling | `https://nova.civai.co/mcp/agents/calendar-agent` | 7 |
| [LienDeadline](https://liendeadline.com) | Statute-cited lien and notice deadlines for material suppliers; lien guides for 50 states and DC. | `https://mcp.liendeadline.com/mcp` | 5 |
| [XposedOrNot Breach Intelligence](https://xposedornot.com/mcp) | Real-time data-breach lookup and analytics for emails and domains from XposedOrNot. | `https://api.xposedornot.com/mcp` | 6 |
| [PokerInk Poker Tools](https://pokerink.com/developers) | Exact Texas Hold'em equity and hand analysis, every runout enumerated. Free, no API key. | `https://pokerink.com/api/mcp` | 3 |
| [PostAgent](https://api.postagent.sh) | Print & mail PDF/HTML/Markdown/text/DOCX/images to US addresses; pay per call in x402 USDC on Base. | `https://api.postagent.sh/mcp` | 14 |
| [FixedQR](https://fixedqr.com) | Generate static QR codes that never expire, as PNG images or SVG. No account or API key needed. | `https://fixedqr.com/mcp` | 3 |
| [Optionscanner](https://optionscanner.ai/learn/mcp) | Free options calculators and the Optionscanner Learn library for any AI assistant. No account. | `https://optionscanner.ai/mcp` | 10 |
| [Lunara Intelligence](https://lunarasociety.com/mcp.html) | EU AI Act and SB 942 obligations for AI systems: each date, the article setting it, signed sources | `https://luiqtimzcsoqnizybifs.supabase.co/functions/v1/lunara-mcp` | 5 |
| [Secret Santa Raffle](https://secretsantaraffle.net/developer-documentation-mcp) | Organise a Secret Santa from Claude or ChatGPT. Matchings never appear in the chat. | `https://mcp.secretsantaraffle.net/claude/mcp` | 3 |
| [checklists](https://wildernesstimes.com/) | Wilderness Times packing checklists, 350+ rated tents and gear buying guides. Free, no signup. | `https://mcp.wildernesstimes.com/mcp` | 7 |
| [LinkPulse](https://linkpulse-neon.vercel.app/) | URL reality check for agents: status, content hash, classification, wayback fallback. | `https://linkpulse-neon.vercel.app/mcp` | 4 |
| [MCPFax Public-Data Utility API](https://mcpscores.com) | One public fact when you have no API key: where, what time, what rate. 31 lookups. | `https://mcpfax-utility.bowling-anthony.workers.dev/mcp` | 31 |
| [TopAlternativesTo](https://topalternatives.to) | Compare software: verified pricing with its source and date, and ranked alternatives. | `https://topalternatives.to/api/mcp/mcp` | 3 |
| [mifactory-pdf](https://github.com/mifactory-bot/mifactory-pdf) | Send transactional pdfs for AI agents via SMTP. Templates included. | `https://mifactory-pdf.vercel.app/mcp` | 4 |

### Other

| Server | What it does | URL | Tools |
|---|---|---|---|
| [CDC Social Vulnerability Index](https://olyport.com) | SVI scores and theme breakdowns by county and tract | `https://mcp.olyport.com/cdc-svi/mcp` | 4 |
| [Semiotic](https://semiotic.nteract.io) | Verified React chart generation: select, validate, repair, render, and inspect charts through MCP. | `https://semiotic-mcp-server-481507046413.us-west1.run.app/mcp` | 5 |
| [GolfCore](https://www.golfcore.org) | AI caddie and flag distances for Premium golfers, plus course maps and tee-specific scorecards. | `https://mcp.golfcore.org/mcp` | 9 |
| [GPH Intelligence - Healthcare Vendor Finder](https://github.com/Crindo2/gph-mcp-server) | Find 76,000+ curated healthcare service vendors across 25 categories and all 50 US states. | `https://gph-mcp-server.pages.dev/mcp` | 4 |
| [SCRIPTMASTERLABS — SqueezeOS MCP](https://www.scriptmasterlabs.com) | SqueezeOS MCP for live machine discovery and x402-paid USDC APIs on Base. | `https://squeezeos-api.onrender.com/mcp?registry=scriptmasterlabs` | 22 |
| [Corbelworks Utility Defect Scan and Buyer Intake](https://corbelworks.pages.dev/utility-defect-scan/) | Preflight utility evidence, open a $149 scan checkout, and file scoped buyer intake. | `https://corbelworks.pages.dev/mcp` | 5 |
| [motion-tools](https://www.mographr.com/mcp) | Render animated motion-graphics overlays as MP4: lower thirds, titles, callouts | `https://mcp.mographr.com/mcp` | 4 |
| [Tarteel MCP Server](https://mcp.tarteel.ai/docs/) | Quran MCP server for translation, tafsir, mutashabihat, recitation playlists, and prayer times. | `https://mcp.tarteel.ai/mcp` | 16 |
| [Call Me](https://serdaroztetik.com/aiphone/) | Your AI rings your iPhone, speaks its question, and gets your spoken answer back as text. | `https://serdaroztetik.com/aiphone/mcp` | 8 |
| [DiffCI](https://diffci.com/mcp-server) | Change-aware CI validation and affected-test guidance for coding agents. | `https://diffci.com/mcp` | 3 |
| [irrational](https://irrational.pages.dev) | Adversarial behavioural-bias engine — audits your decisions for cognitive biases via your own AI. | `https://irrational.pages.dev/mcp/server` | 3 |
| [Local Pros by Ron Ventures](https://ronventures.pages.dev/connector) | Find owner-operated plumbers, HVAC techs, electricians and roofers in OK, KS, NE, IA and MO. | `https://ronventures.pages.dev/mcp` | 3 |
| [THORChain Swap](https://swap.thorchain.org/developers/mcp) | Read-only THORChain swap quotes, liquidity pools, and network status. | `https://swap.thorchain.org/mcp` | 3 |
| [Call Me](https://callmemcp.com/) | Your AI rings your iPhone, speaks its question, and gets your spoken answer back as text. | `https://callmemcp.com/mcp` | 8 |
| [Forge Treasury](https://github.com/forge-treasury/forge-cursor-plugin) | Non-custodial USDC yield vaults on Base mainnet with 9 MCP tools for AI agent treasury. | `https://mcp.forgetreasury.com/mcp` | 9 |
| [FDA import alert red lists](https://referencesource.org/fda-import-alert-red-list) | Is a foreign supplier on an FDA import alert red list, detained at the US border? 14,000+ listings. | `https://referencesource.org/mcp/import-alerts` | 6 |
| [RunBoth](https://runboth.dev) | Ask runboth.dev in plain language: what RunBoth does, how to install it, and its limits. | `https://runboth-agent-mgbxvs4loq-uc.a.run.app/mcp` | 3 |
| [Trust Gate](https://trust-gate-mcp.onrender.com) | Post-quantum, tamper-evident receipts for agent actions. Ed25519 + ML-DSA-65, offline verify. | `https://trust-gate-mcp.onrender.com/mcp` | 7 |
| [SolvScore](https://solvscore.com) | Credit scores for AI agents. Underwrite an unknown counterparty before extending credit. | `https://solvscore.com/mcp` | 20 |
| [AIDISH — AIエージェントから受取注文できる飲食店](https://aidish-app.onrender.com/agents) | Pickup orders at Japanese restaurants for AI agents: find stores, read menus, place orders. No auth. | `https://aidish-app.onrender.com/mcp` | 4 |
| [agent-resolve-mcp](https://github.com/agent-resolve/agent-resolve-mcp) | Escrow, verification, and settlement platform for AI agents hiring other AI agents. | `https://agent-resolve-mcp.onrender.com/mcp` | 7 |
| [NovaRail](https://agentnet-api.onrender.com/connect) | Discover, verify, and hire AI agents from the NovaRail marketplace, from your editor. | `https://agentnet-api.onrender.com/mcp` | 10 |
| [Dantes Exchange](https://dantes.ai) | Paid trader skills MCP. Coil scanner with dated 252d forward-return evidence. x402 USDC. | `https://dantes.ai/exchange/mcp` | 8 |
| [CalRisk Insurance Center](https://douxprocess.com/agency/calrisk-insurance-center) | Licensed CA agency: GL, workers' comp, auto, bonds. Check appetite or send a quote request. | `https://douxprocess.com/mcp/a/calrisk-insurance-center` | 4 |
| [SKUit Network & Security Catalog](https://skuit.ai) | AI helper for choosing and speccing network & security products from Cisco, Arista, Juniper and more | `https://mcp.skuit.ai/api/mcp/catalog` | 3 |

## Method

1. `scripts/fetch_registry.py` reads every server (latest version) from the registry and keeps remote endpoints.
2. `scripts/probe.py` tests Streamable HTTP endpoints that need no headers, at most 5 URLs per host, no temporary tunnels, 10 s timeout.
3. `scripts/make_directory.py` drops mass-generated copies (same tool set more than 3 times, same description more than twice, more than 2 per domain) and assigns topics by keyword.

The workflow in `.github/workflows/weekly.yml` runs this every Monday and commits the result. Data: CC BY 4.0. Code: MIT.

Maintained by [Shortform Kit](https://shortformkit.com), which runs its own free remote MCP server for social video transcripts and creator data: `https://shortformkit.com/mcp`.

