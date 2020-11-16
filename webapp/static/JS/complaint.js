// Setting registered date time
let regDateTimeElement = document.getElementById('reg-date-time');

let h = rdt.getHours(), m = rdt.getMinutes(), ap = (h >= 12) ? 'pm' : 'am';
let hh = (h > 12) ? h - 12 : h; hh = (hh < 10) ? '0' + hh : hh; m = (m < 10) ? '0' + m : m;
let D = rdt.getDate(), M = rdt.getMonth() + 1, YYYY = rdt.getFullYear();
regDateTimeElement.innerText = 'Registered at ' + hh + ':' + m + ' ' + ap + ' on ' + D + '/' + M + '/' + YYYY;