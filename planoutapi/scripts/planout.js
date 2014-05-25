jQuery(document).ready( function($) {

    //var clientId = localStorage.getItem('clientId');
    var clientId = null;

    if (clientId == null) {
        clientId = Math.floor((Math.random() * 100000) + 1);
        localStorage.setItem('clientId', clientId);
        ga('set', 'dimension2', clientId); // pass the client id to GA
    }

    var api = "http://162.243.42.182:8999/hpexp/".concat(clientId);
    console.log(api);

    $.ajax({
            url : api,
            type: 'GET',
            dataType: 'jsonp',
            jsonpCallback: "localcallback",
            success: function (data) {

                var data = $.parseJSON(data);
                console.log(data);

                if (data['style'] == true && data['greeting_text'] != "") {
                    $("#style").addClass("alert alert-info");
                }

                $("#expA").html(data['greeting_text']);
            }
    })

});
