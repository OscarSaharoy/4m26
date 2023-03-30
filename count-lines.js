import bst from "./bst.json" assert { type: "json" };

const cellLineCounts = bst.cells.map( cell => cell.source.length );
console.log(cellLineCounts.reduce( (acc,val) => acc + val, 0 ))

//const filename = process.argv[2];
