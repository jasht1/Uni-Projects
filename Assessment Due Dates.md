
```mermaid
---
displayMode: compact
---
gantt
title 4 months of uni timeline
dateFormat YYYY-MM-DD
tickInterval 2week

section Industrial Automation
	Pneumatics Due: done, milestone, 2025-03-13, 1d
	Electro-Pneumatics: crit, milestone, 2025-04-17, 1d
	Report: crit, milestone, 2025-05-22, 1d
section Robotics 
	Assignment: done, milestone, 2025-03-27, 1d
	Project: crit, milestone, 2025-05-22, 1d
section Building Systems
	SOA: crit, milestone, 2025-04-03, 1d
	Design Project: crit, milestone, 2025-06-05, 1d 
section Signal Processing
	Assignment: crit, milestone, 2025-04-24, 1d
	TCA: crit, milestone, 2025-05-12, 1d
section Individual Project
	Diss: crit, milestone, 2025-05-08, 1d
	Poster: crit, milestone, 2025-05-15, 1d
```

```dataview
TABLE link(dateformat(due,"yyyy-MM-dd"),dateformat(due,"yyyy-MM-dd")) AS "Due Date", due - date(today) AS "Due In", weight + "%" AS "Weight", substring(module, 8) as Module
FROM "Projects/Uni Projects" AND #Assessment
WHERE due > date(today)
SORT due 
```
