[All SpreadSheets can be found here in the working repository](https://github.com/jasht1/Uni-Projects/tree/master/Energy%20Systems%20and%20Conversion/CourseWork/attachments/SpreadSheets)

### Lab_Readings
```dataviewjs
const RelativePath = 'Lab Readings - Energy Systems and Conversion Coursework.csv';
const csvFile = await dv.io.load(RelativePath);
const rows = csvFile.split("\n").map(row => row.split(","));
const headers = rows[0];
const data = rows.slice(1);

dv.table(headers, data);
```

### All_Data
```dataviewjs
const FilePath = dv.current().file.path;
const CurrentPath = FilePath.substring(0, FilePath.lastIndexOf('/'));
const RelativePath = "All Data.csv";
const Path = CurrentPath +"/"+ RelativePath;
const csvFile = await dv.io.load(Path);
const rows = csvFile.split("\n").map(row => row.split(","));
const headers = rows[0];
const data = rows.slice(1);

dv.table(headers, data);
```
