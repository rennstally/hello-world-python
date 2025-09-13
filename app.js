let bill = prompt("Enter the bill amount:");
bill = Number(bill);
console.log("Bill:", bill);

let tipPercent = prompt("Enter tip percentage (e.g. 15 for 15%):");
tipPercent = Number(tipPercent);

let tip = bill * (tipPercent / 100);
let total = bill + tip;

let people = prompt("How many people are splitting the bill?");
people = Number(people);

let perPerson = total / people;

alert("Tip: $" + tip.toFixed(2) + 
      "\nTotal: $" + total.toFixed(2) + 
      "\nEach person pays: $" + perPerson.toFixed(2));
