#!/usr/bin/node

const esrever = (list) => {
  const reversedArray = [];
  list.forEach((e) => reversedArray.unshift(e));
  return (reversedArray);
};

module.exports = { esrever };
