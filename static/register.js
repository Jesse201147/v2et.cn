var check_name = function (ele) {
    if (ele.value.length < 3) {
        ele.parentElement.querySelector('small').style.visibility = 'visible';
    } else {
        ele.parentElement.querySelector('small').style.visibility = 'hidden';
        check_form()
    }
};
var check_em = function (ele) {
    var email = ele.value;
    var reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
    if (email != "") {
        is_ok = reg.test(email);
        if (is_ok) {
            ele.parentElement.querySelector('small').style.visibility = 'hidden';
            check_form()
        } else {
            ele.parentElement.querySelector('small').style.visibility = 'visible';
        }
    } else {
        ele.parentElement.querySelector('small').style.visibility = 'visible';
    }
};
var check_pw1 = function (ele) {
    if (ele.value.length < 6) {
        ele.parentElement.querySelector('small').style.visibility = 'visible';
    } else {
        ele.parentElement.querySelector('small').style.visibility = 'hidden';
        check_pw2(document.getElementById('password2'))
    }
};
var check_pw2 = function (ele) {
    if (document.getElementById('password').value != document.getElementById('password2').value) {
        ele.parentElement.querySelector('small').style.visibility = 'visible';
    } else {
        ele.parentElement.querySelector('small').style.visibility = 'hidden';
        check_form()
    }
};
var check_form = function () {
    if (document.getElementById('submit').disabled == true) {
        var count = 0;
        $('form>div').each(function () {
            if (this.querySelector('input').value.length > 1) {
                count++;
                console.log(count);
            }
            if (this.querySelector('small').style.visibility == 'hidden') {
                count++;
                console.log(count);
            }
        });
        if (count == 8) {
            document.getElementById('submit').disabled = false;
            // document.getElementById('submit').click();
            document.getElementById('button_tip').style.visibility = 'hidden';
        } else {
            document.getElementById('button_tip').style.visibility = 'visible';
        }
    }
};