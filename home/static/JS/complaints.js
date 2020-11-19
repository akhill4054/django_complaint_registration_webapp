let list = document.getElementById('main-col');

function formattedComplaintDateTime(rdt) {
    let h = rdt.getHours(), m = rdt.getMinutes(), ap = (h >= 12) ? 'pm' : 'am';
    let hh = (h > 12) ? h - 12 : h; hh = (hh < 10) ? '0' + hh : hh; m = (m < 10) ? '0' + m : m;
    let D = rdt.getDate(), M = rdt.getMonth() + 1, YYYY = rdt.getFullYear();
    return 'Registered at ' + hh + ':' + m + ' ' + ap + ' on ' + D + '/' + M + '/' + YYYY;
}

// Converting UTC date time string to formatted local date time for each list item
for (let i = 0; i < list.children.length - 1; i++) {
    let dateTimeField = list.children[i].children[0].children[0];
    let rdt = new Date(dateTimeField.innerText + 'Z');
    dateTimeField.innerText = formattedComplaintDateTime(rdt);
}