var isCheckedsign = false;
var isChecked = false;
var toggleId = 0;
function changeTextById(id, newText) {
    var element = document.getElementById(id);
    if (element) {
        element.innerText = newText;
    } else {
        console.error("Element with id " + id + " not found.");
    }
}
function refreshstate(isChecked=false, toggleId=0, isCheckedsign) {
    console.log(isCheckedsign)
    $.ajax({
        url: '/update_toggle',
        type: 'POST',
        data: { id: toggleId, status: isChecked, sign: isCheckedsign},
        success: function(response) {
            console.log(response);
            for(i = 0; i < 8; i++) {
            $(`#displaytoggle${Number(i)}`).prop('checked', response[0][1][i]);
            }
            $(`#overbufferedtoggle`).prop('checked', response[0][0]);
            changeTextById('int10_0', response[1]);
            changeTextById('int10_1', response[2]);
            changeTextById('int10_2', response[3]);
        },
        error: function(xhr, status, error) {
            console.error('Request failed with status: ' + xhr.status);
        }
    });
};
$(document).ready(function() {
    $('.toggle-switch input').change(function() {
        isChecked = $(this).prop('checked') ? true : false; 
        toggleId = $(this).attr('id');
        refreshstate(isChecked, toggleId, isCheckedsign)
    });
});

$(document).ready(function(){
    $('#btn-checkbox').change(function(){
        isCheckedsign = !(isCheckedsign);
        if (isCheckedsign) {
            changeTextById("num0", "-128")
            changeTextById("num00", "-128")
            changeTextById("num000", "-128")
        }
        else {
            changeTextById("num0", "128")
            changeTextById("num00", "128")
            changeTextById("num000", "128")
        }
        refreshstate(isChecked, toggleId, isCheckedsign)
    });
});