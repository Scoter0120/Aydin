function init() {
    showDataList();
};

function gather() {
    var category = $("#category").val();
    var value = $("#value").val();
    var dataDate = $("input[name='dataDate']").val();
    if (category.length == 0 || value.length == 0 || dataDate.length == 0) {
        alert("内容不能为空！");
        return;
    }
    var msg = "您确定添加/更新此项内容吗？";
    if (confirm(msg) == true) {
        $.ajax({
            url: '/scoter/gather',
            type: 'get',
            data: {category: category, value: value, dataDate: dataDate },
            dataType: 'JSON',
            success: function (data) {
                if (data) {
                    alert("添加/更新成功！");
                } else {
                    alert("添加/更新失败！");
                }
                showDataList();
            }
        });
    }
}

function showDataList() {
    $("#table").datagrid({
        url: '/scoter/showData',
        method: 'GET',
        pagination: true,
        pageNumber: 1,
        pageSize: 10,
        pageList: [10, 20],
        rownumbers: true,
        columns: [[{
            title: '工厂(默认)',
            field: 'FACTORY',
            sortable: true,
            width: 100
        }, {
            title: '类别',
            field: 'CATEGORY',
            sortable: true,
            width: 120
        }, {
            title: '值',
            field: 'VALUE',
            sortable: true,
            width: 120
        }, {
            title: '日期',
            field: 'DATA_DATE',
            sortable: true,
            width: 150
        }, {
            title: '更新时间',
            field: 'UPDATE_TIME',
            sortable: true,
            width: 150
        }]]
    });
}

function refresh() {
    showDataList();
}

function myformatter(date) {
    var y = date.getFullYear();
    var m = date.getMonth() + 1;
    var d = date.getDate();
    return y + '-' + (m < 10 ? ('0' + m) : m) + '-' + (d < 10 ? ('0' + d) : d);
}
function myparser(s) {
    if (!s) return new Date();
    var ss = (s.split('-'));
    var y = parseInt(ss[0], 10);
    var m = parseInt(ss[1], 10);
    var d = parseInt(ss[2], 10);
    if (!isNaN(y) && !isNaN(m) && !isNaN(d)) {
        return new Date(y, m - 1, d);
    } else {
        return new Date();
    }
}