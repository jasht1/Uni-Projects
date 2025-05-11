
```mermaid
---
displayMode: compact
---
gantt
title Last Semester of Uni
dateFormat YYYY-MM-DD
tickInterval 2week

section Industrial Automation
	Pneumatics Due: done, milestone, 2025-03-13, 1d
	Electro-Pneumatics: done, milestone, 2025-04-17, 1d
	Group Assignment: crit, milestone, 2025-05-22, 1d
section Robotics
	Assignment: done, milestone, 2025-03-27, 1d
	Group Project: crit, milestone, 2025-05-22, 1d
section Building Systems
	SOA: done, milestone, 2025-04-03, 2025-04-10
	Design Project: crit, milestone, 2025-06-05, 2025-06-05
section Signal Processing
	Assignment: done, milestone, 2025-04-24, 2025-04-27
	TCA: crit, milestone, 2025-05-23, 1d
section Individual Project
	Diss: done, milestone, 2025-05-08, 1d
	Poster: crit, milestone, 2025-05-15, 1d
```

```dataview
TABLE
link(dateformat(due,"yyyy-MM-dd"),
dateformat(due,"yyyy-MM-dd")) AS "Due Date",
due - date(dateformat(date(now), "yyyy'yr 'M'mo 'd'd 'h'h '"), "yyyy'yr 'M'mo 'd'd 'h'h '") AS "Due In",
weight + "%" AS "Weight", substring(module, 8) as Module
FROM "Projects/Uni Projects" AND #Assessment
WHERE due > date(today)
SORT due
```

