const sqlite3 = require('sqlite3').verbose();

// 连接数据库
let db = new sqlite3.Database('/Users/makaka/code-repository/makaka/sqlite3操作/student.db', (err) => {
    if (err) {
      return console.error(err.message);
    }
    console.log('Connected to the in-memory SQlite database.');
  });

  // db.all(sql, [], (err, rows) => {
  //   if (err) {
  //     throw err;
  //   }
  //   rows.forEach((row) => {
  //     console.log(row);
  //   });
  // });

  // db.serialize(() => {
  //   db.each(`SELECT Id as id,
  //                   name as name
  //            FROM student`, (err, row) => {
  //     if (err) {
  //       console.error(err.message);
  //     }
  //     console.log(row.id + "\t" + row.name);
  //   });
  // });

let sql = `SELECT * from student where Id = Count(name)`;
let sql1 = `SELECT Count(name) from student`;
db.each(sql1, [], (err, row) => {
  if (err) {
    throw err;
  }
  console.log(`${row.name}`);
});