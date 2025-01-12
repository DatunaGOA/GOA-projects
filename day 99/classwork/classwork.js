//1
function n(sets) {
    let acc = new Set();
    for (let set of sets) {
      for (let value of set) {
        acc.add(value);
      }
    }
    return acc;
  }
  console.log(n([new Set([1, 2]), new Set([2, 3]), new Set([3, 4])]));


//2

  function s(str) {
    const map = new Map();
    for (let char of str) {
      map.set(char, (map.get(char) || 0) + 1);
    }
    return map;
  }
  
  console.log(s("hello"));

//3



function i(map) {
    const mapinvert = {};
    for (let [key, value] of map) {
      mapinvert[value] = key;
    }
    return mapinvert;
  }
  
  console.log(i(new Map([['a', 1], ['b', 2], ['c', 1]])));
  