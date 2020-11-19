function buildRow() {
    return "<div class='row mb-3'></div>"
}

function buildItem(category) {
    return "<div id='list-item' class='col-4 pr-5' onclick=\"itemClickListener('" + category + "')\">"
    + "<div class='btn btn-primary card pl-3 pr-3 pt-3'>"
    + "<div class='row justify-content-center'>"
    + "<p class='h4 text-dark border-bottom'>" + category + "</p>"
    + "</div>"
    + "<div class='mt-3 row justify-content-center'>"
    + "<h5> <span class='text-dark'>" + metaInf[category] + " complaints</span></h5>"
    + "</div>"
    + "</div>"
    + "</div>";
}

// Click listsners
function itemClickListener(category) {
    window.location.href = 'browse/category/' + category + '/1';
}

let searchInput = document.getElementById('search-box');

function search() {
    let complaintId = searchInput.value;
    if (complaintId != '') {
        window.location.href = 'browse/complaint/' + complaintId;
    } else {
        alert('Complaint id is empty!');
    }
}

// Building list
// Generating rows
let mainColumn = document.getElementById('main-col');
let temp = "";
for (let i = 0; i < categories.length / 3; i++) {
    temp += buildRow();
}
mainColumn.innerHTML = temp;

// Generating list items
let row = 0;
for (let i = 0; i < categories.length; i++) {
    let rowElement = mainColumn.children[row];
    rowElement.innerHTML += buildItem(categories[i]);
    if ((i + 1) % 3 == 0) row++;
}