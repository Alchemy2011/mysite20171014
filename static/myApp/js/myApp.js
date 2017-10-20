/**
 * Created by dell on 2017/10/18.
 */
console.log("good app");

// 比较简陋的ajax，标准的不是这样
$(document).ready(function displayDate(){
	document.getElementById("btn").onclick =
    function () {
	    $.ajax({
            type:"get",
            url:"/myapp/studentsinfo/",
            dataType:"json",
            success:function (data, status) {
                console.log(data);
                var d = data["data"];
                for(var i = 0;i<d.length;i++){
                    document.write('<p>'+d[i][0]+'</p>')
                }
            }
        })
    };
});
