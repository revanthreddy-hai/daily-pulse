#!/usr/bin/env python3
"""Generate public demo Daily Pulse pages for a backfilled date range.

This is intentionally deterministic and public-source only. It is for demos,
not private Slack/local Pulse content.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from html import escape
from pathlib import Path


SITE_DIR = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/revanthreddy-hai/daily-pulse"
PUBLIC_BASE = "https://revanthreddy-hai.github.io/daily-pulse/"
START = date(2026, 5, 1)
END = date(2026, 5, 10)


@dataclass(frozen=True)
class Card:
    day: date
    kind: str
    label: str
    title: str
    body: str
    source_label: str
    source_url: str
    why: str


ICON_FOR = {
    "one-move": "one-move.svg",
    "external": "runtime.svg",
    "learning": "paper.svg",
    "infra": "mesh.svg",
    "contribution": "contribution.svg",
    "private": "private.svg",
}


EVERGREEN = [
    Card(
        START,
        "infra",
        "SERVICE MESH",
        "Istio + Gateway API Inference Extension",
        "Istio documents AI-aware traffic management through Gateway API Inference Extension, routing by model-serving semantics instead of plain HTTP.",
        "Istio docs",
        "https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api-inference-extension/",
        "Baseline for LLM routing behind a mesh.",
    ),
    Card(
        START,
        "contribution",
        "OPPORTUNITY",
        "Gateway API Inference Extension upstream",
        "The Kubernetes SIG project defines the CRDs and endpoint-picker surface for inference routing. Issues and docs gaps are a clean open-source contribution path.",
        "kubernetes-sigs repo",
        "https://github.com/kubernetes-sigs/gateway-api-inference-extension",
        "Track where mesh-level LLM routing is heading.",
    ),
]


TIMELINE = [
    Card(
        date(2026, 5, 1),
        "infra",
        "KUBERNETES",
        "Pod-level resource managers enter alpha",
        "Kubernetes v1.36 added alpha pod-level resource managers. For serving workloads, this is worth tracking because resource control keeps moving closer to the pod boundary.",
        "Kubernetes blog",
        "https://kubernetes.io/blog/2026/05/01/kubernetes-v1-36-feature-pod-level-resource-managers-alpha/",
        "Useful for capacity and scheduling mental models.",
    ),
    Card(
        date(2026, 5, 1),
        "external",
        "LLM-D",
        "llm-d v0.7.0 release candidates start",
        "llm-d published v0.7.0 release candidates on May 1, including fixes around images and connectors. Watch the project as Kubernetes-native LLM serving patterns mature.",
        "llm-d v0.7.0-rc.2",
        "https://github.com/llm-d/llm-d/releases/tag/v0.7.0-rc.2",
        "Good reference for disaggregated serving design.",
    ),
    Card(
        date(2026, 5, 2),
        "learning",
        "ROUTING",
        "Inference-aware traffic beats round-robin",
        "Istio's AI-aware traffic-management write-up explains why generic load balancing falls short for LLM traffic and how inference-extension endpoints can route by queue and cache state.",
        "Istio blog",
        "https://istio.io/latest/blog/2025/inference-extension-support/",
        "Frames prefix/cache-aware routing decisions.",
    ),
    Card(
        date(2026, 5, 3),
        "external",
        "VLLM",
        "vLLM v0.20.2 rc appears",
        "vLLM published a v0.20.2 release candidate on May 3. Release candidates are useful early warning for API and runtime changes before stable patches land.",
        "vLLM rc",
        "https://github.com/vllm-project/vllm/releases/tag/v0.20.2rc0",
        "Early signal for serving-stack changes.",
    ),
    Card(
        date(2026, 5, 4),
        "infra",
        "KUBERNETES",
        "Admission policies that cannot be deleted",
        "Kubernetes v1.36 highlighted manifest-based admission control. For platform work, deletion-resistant policy paths matter when guardrails need to survive drift.",
        "Kubernetes blog",
        "https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/",
        "Useful for policy guardrail design.",
    ),
    Card(
        date(2026, 5, 4),
        "external",
        "VLLM",
        "vLLM v0.20.1 stable release",
        "vLLM v0.20.1 landed as a stable release. Keep stable runtime releases in the Pulse because small serving changes can look like application-level reliability symptoms.",
        "vLLM v0.20.1",
        "https://github.com/vllm-project/vllm/releases/tag/v0.20.1",
        "Pin or test before broad rollout.",
    ),
    Card(
        date(2026, 5, 5),
        "infra",
        "KUBERNETES",
        "Declarative validation graduates to GA",
        "Kubernetes v1.36 moved declarative validation to GA. This is relevant for infra-agent safety because APIs with clearer validation boundaries are easier to reason about.",
        "Kubernetes blog",
        "https://kubernetes.io/blog/2026/05/05/kubernetes-v1-36-declarative-validation-ga/",
        "Sharpens API-boundary thinking.",
    ),
    Card(
        date(2026, 5, 5),
        "external",
        "SGLANG",
        "SGLang v0.5.11 ships",
        "SGLang v0.5.11 landed on May 5. Runtime release notes are worth skimming for scheduler, cache, tokenizer, and server-stability changes.",
        "SGLang v0.5.11",
        "https://github.com/sgl-project/sglang/releases/tag/v0.5.11",
        "Upstream awareness for serving reliability.",
    ),
    Card(
        date(2026, 5, 5),
        "external",
        "LLM-D",
        "llm-d v0.7 release line continues",
        "llm-d published more v0.7 release candidates on May 5. The project is a good public reference for disaggregated prefill/decode and routing integration.",
        "llm-d v0.7.0-rc.3",
        "https://github.com/llm-d/llm-d/releases/tag/v0.7.0-rc.3",
        "Follow scheduler and routing integration.",
    ),
    Card(
        date(2026, 5, 6),
        "infra",
        "KUBERNETES",
        "Server-side sharded list and watch",
        "Kubernetes v1.36 covered server-side sharded list and watch. Controller scalability signals are useful when thinking about observability and control-plane load.",
        "Kubernetes blog",
        "https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/",
        "Useful for large-cluster controller design.",
    ),
    Card(
        date(2026, 5, 6),
        "external",
        "CLAUDE CODE",
        "Claude Code release cadence stays active",
        "Claude Code published multiple releases around May 6. Tooling release cadence matters because coding-agent workflows can change underneath daily engineering habits.",
        "Claude Code releases",
        "https://github.com/anthropics/claude-code/releases/tag/v2.1.132",
        "Watch developer-agent ergonomics.",
    ),
    Card(
        date(2026, 5, 7),
        "infra",
        "KUBERNETES",
        "DRA gets more drivers and features",
        "Kubernetes v1.36 highlighted the next DRA wave. Dynamic Resource Allocation remains relevant to GPU and accelerator-backed serving fleets.",
        "Kubernetes blog",
        "https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/",
        "Track accelerator scheduling direction.",
    ),
    Card(
        date(2026, 5, 7),
        "learning",
        "CACHE",
        "MLA-native position-independent caching",
        "A new arXiv paper quantifies TTFT spikes when bit-identical tokens shift position across turns and proposes a correction. It is useful for cache-hit invariant thinking.",
        "arXiv 2605.05696",
        "https://arxiv.org/abs/2605.05696",
        "Good reading for LLM-serving performance.",
    ),
    Card(
        date(2026, 5, 8),
        "infra",
        "KUBERNETES",
        "Volume Group Snapshots move to GA",
        "Kubernetes v1.36 moved Volume Group Snapshots to GA. It is less LLM-serving-specific, but it matters for stateful platform recovery and backup semantics.",
        "Kubernetes blog",
        "https://kubernetes.io/blog/2026/05/08/kubernetes-v1-36-volume-group-snapshot-ga/",
        "Useful for recovery planning vocabulary.",
    ),
    Card(
        date(2026, 5, 8),
        "external",
        "CODEX",
        "Codex CLI v0.130.0 lands",
        "OpenAI Codex CLI published v0.130.0 on May 8. Keep an eye on coding-agent release notes because site generation and visual QA can move into repeatable automation.",
        "Codex v0.130.0",
        "https://github.com/openai/codex/releases/tag/rust-v0.130.0",
        "Relevant to agent-built static sites.",
    ),
    Card(
        date(2026, 5, 9),
        "external",
        "CODEX",
        "Codex alpha releases continue",
        "Codex CLI alpha releases continued on May 9. Fast-moving agent tooling is worth tracking when the workflow itself is becoming part of the engineering system.",
        "Codex releases",
        "https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.4",
        "Watch for automation and review improvements.",
    ),
    Card(
        date(2026, 5, 9),
        "external",
        "CLAUDE CODE",
        "Claude Code v2.1.138 appears",
        "Claude Code v2.1.138 landed on May 9. For a mixed Codex/Claude workflow, release awareness helps explain why automation behavior changes.",
        "Claude Code v2.1.138",
        "https://github.com/anthropics/claude-code/releases/tag/v2.1.138",
        "Track headless-agent behavior shifts.",
    ),
    Card(
        date(2026, 5, 10),
        "external",
        "VLLM",
        "vLLM v0.20.2 ships stable fixes",
        "vLLM v0.20.2 shipped on May 10 with hang and KV-block related fixes. Stable serving-runtime fixes belong in the daily watch list because they can masquerade as app issues.",
        "vLLM v0.20.2",
        "https://github.com/vllm-project/vllm/releases/tag/v0.20.2",
        "Scan before diagnosing model-slow symptoms.",
    ),
    Card(
        date(2026, 5, 10),
        "external",
        "CODEX",
        "Codex v0.131.0 alpha advances",
        "OpenAI Codex published another v0.131.0 alpha on May 10. It is relevant because Codex can own the website build and browser screenshot QA loop.",
        "Codex alpha",
        "https://github.com/openai/codex/releases/tag/rust-v0.131.0-alpha.5",
        "Potential upgrade for visual QA workflows.",
    ),
]


def e(value: str) -> str:
    return escape(value, quote=True)


def date_label(day: date) -> str:
    return day.strftime("%b %d").replace(" 0", " ")


def archive_label(day: date) -> str:
    return day.strftime("%b %d, %Y").replace(" 0", " ")


def card_html(card: Card, prefix: str = "") -> str:
    icon = ICON_FOR.get(card.kind, "runtime.svg")
    priority = " priority" if card.kind == "one-move" else ""
    return f'''      <article class="pulse-card{priority}">
        <img src="{prefix}assets/img/{e(icon)}" alt="" class="thumb">
        <div class="card-copy">
          <p class="label">{e(card.label)}</p>
          <h2>{e(card.title)}</h2>
          <p>{e(card.body)}</p>
          <div class="card-meta">
            <a href="{e(card.source_url)}" rel="noreferrer">{e(card.source_label)}</a>
            <span>{e(card.why)}</span>
          </div>
        </div>
      </article>'''


def select_cards(day: date) -> list[Card]:
    available = [card for card in TIMELINE if card.day <= day]
    latest_by_label: dict[str, Card] = {}
    for card in available:
        latest_by_label[card.label] = card

    selected: list[Card] = []
    for label in ["KUBERNETES", "VLLM", "SGLANG", "LLM-D", "CODEX", "CLAUDE CODE", "CACHE"]:
        card = latest_by_label.get(label)
        if card and card not in selected:
            selected.append(card)

    # Put the most recent date-specific cards first, then evergreen contribution/routing cards.
    selected = sorted(selected, key=lambda card: (card.day, card.label), reverse=True)[:4]
    selected.extend(EVERGREEN)
    return selected[:6]


def nav_html(context: str) -> str:
    if context == "latest":
        first = '<a class="icon-link" href="archive/" title="Past pulses" aria-label="Past pulses"><span data-lucide="calendar-days"></span></a>'
    elif context == "date":
        first = '<a class="icon-link" href="../" title="Latest pulse" aria-label="Latest pulse"><span data-lucide="arrow-left"></span></a><a class="icon-link" href="../archive/" title="Past pulses" aria-label="Past pulses"><span data-lucide="calendar-days"></span></a>'
    else:
        first = '<a class="icon-link" href="../" title="Latest pulse" aria-label="Latest pulse"><span data-lucide="arrow-left"></span></a>'
    return f'''{first}
      <a class="primary-action" href="{REPO_URL}" title="Open source repository">
        <span data-lucide="github"></span>
        <span>Source</span>
      </a>'''


def render_pulse(day: date, cards: list[Card], prefix: str, context: str) -> str:
    card_block = "\n\n".join(card_html(card, prefix) for card in cards)
    latest_note = " Public demo backfill." if day < END else ""
    intro = (
        "Signals at the intersection of Kubernetes, LLM serving, service mesh, "
        f"and coding agents worth a scan today.{latest_note}"
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>Daily Pulse - {e(date_label(day))}</title>
  <link rel="stylesheet" href="{prefix}assets/css/pulse.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="{prefix or './'}" aria-label="Daily Pulse home">Daily Pulse</a>
    <nav class="nav-actions" aria-label="Pulse actions">
      {nav_html(context)}
    </nav>
  </header>

  <main class="pulse-shell">
    <section class="intro" aria-labelledby="pulse-title">
      <p class="kicker">Morning intelligence</p>
      <h1 id="pulse-title">{e(date_label(day))}</h1>
      <p class="lede">{e(intro)}</p>
    </section>

    <section class="feed" aria-label="Daily Pulse cards">
{card_block}
    </section>
  </main>

  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script>
    lucide.createIcons({{ strokeWidth: 2 }});
  </script>
</body>
</html>
'''


def render_archive(days: list[date]) -> str:
    rows = "\n".join(
        f'''      <a class="archive-row" href="../{day.isoformat()}/">
        <span>{e(archive_label(day))}</span>
        <strong>Open pulse</strong>
      </a>'''
        for day in sorted(days, reverse=True)
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>Daily Pulse Archive</title>
  <link rel="stylesheet" href="../assets/css/pulse.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="../" aria-label="Daily Pulse home">Daily Pulse</a>
    <nav class="nav-actions" aria-label="Pulse actions">
      {nav_html("archive")}
    </nav>
  </header>

  <main class="pulse-shell">
    <section class="intro" aria-labelledby="pulse-title">
      <p class="kicker">Archive</p>
      <h1 id="pulse-title">Past Pulses</h1>
      <p class="lede">Browse previous public Daily Pulse pages.</p>
    </section>

    <section class="archive-list" aria-label="Past Daily Pulses">
{rows}
    </section>
  </main>

  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script>
    lucide.createIcons({{ strokeWidth: 2 }});
  </script>
</body>
</html>
'''


def main() -> None:
    days = [START + timedelta(days=offset) for offset in range((END - START).days + 1)]
    for day in days:
        target = SITE_DIR / day.isoformat()
        target.mkdir(parents=True, exist_ok=True)
        (target / "index.html").write_text(render_pulse(day, select_cards(day), "../", "date"))

    (SITE_DIR / "index.html").write_text(render_pulse(END, select_cards(END), "", "latest"))
    (SITE_DIR / "archive").mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "archive" / "index.html").write_text(render_archive(days))

    # Keep legacy archive/date.html links working while dated directories are the canonical shape.
    for day in days:
        (SITE_DIR / "archive" / f"{day.isoformat()}.html").write_text(
            render_pulse(day, select_cards(day), "../", "archive")
        )

    print(f"Generated {len(days)} demo pulses: {PUBLIC_BASE}2026-05-01/ ... {PUBLIC_BASE}2026-05-10/")


if __name__ == "__main__":
    main()
