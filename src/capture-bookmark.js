const fs = require('fs');
const util = require('./util');

async function captureBookmark(customOutDir, filePath, start, end) {
  const outPath = util.getOutPath(customOutDir, filePath, "bookmark.txt");
  const buf = `${start}|${end}\n`;
  await fs.appendFile(outPath, buf);
  return util.transferTimestamps(filePath, outPath);
}

module.exports = captureBookmark;