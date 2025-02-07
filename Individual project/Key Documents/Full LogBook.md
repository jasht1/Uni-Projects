
```mermaid
---
displayMode: compact
---
gantt
title Project Timeline

dateFormat YYYY-MM-DD
excludes Christmas: 2024-12-20 to 2025-01-07, Exam week 1: 2025-01-14 to 2025-01-24, Exam week 2: 2025-04-15 to 2025-04-26

section Project Admin
	Ethics Subforms : crit, done, 2024-10-25, 4d
	Project Proposal : crit, done, 2024-10-27, 2024-11-07
	Interim Report : crit, active, 2024-12-25, 2025-02-06
	Interim Presentation : milestone, 2025-02-12, 1d
	Final Report : crit, 2025-04-01, 2025-05-08
	Poster : 2025-05-01, 2025-05-12

section Research
	Anatomy & Physiology : done, 2024-10-13, 45d
	Contact Models : done, 1M
	Pathophysiology: done, 1M
	FD analysis: active, 1M

section Investigation
	Learning Curve: 2024-12-03, 10d
	Data Processing :2025-02-07 , 40d
	Data Analysis : 1M

```

```dataview
CALENDAR file.ctime

FROM "Projects/Uni Projects/Individual project/Notes"
```

```dataview
Table 
	regexreplace(file.folder, ".*\/", "") AS Type,
	file.cday AS Created,
	file.mday AS Modified

FROM "Projects/Uni Projects/Individual project/Notes/Logs" OR "Projects/Uni Projects/Individual project/Notes/Meetings"
SORT file.ctime
```
