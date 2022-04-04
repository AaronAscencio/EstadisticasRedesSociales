
function message_error(obj) {
    
    let html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    }
    else{
        html = '<p>'+obj+'</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html, 
        icon: 'error'
    });
}


$(function(){

    $(".btnModal").on('click',function(){
        $('#modalEncuesta').modal('show');
    });

    $('form').on('submit',function(e){
        e.preventDefault();
        let params = new FormData(this);
        console.log(params);
        send_with_ajax(window.location.pathname,params,function(){
            location.reload();
        });
    });

    let ctx = document.getElementById('myChart').getContext('2d');
    let myChart = new Chart(ctx, { 
        type: 'bar',
        data: {
            labels: ['Facebook', 'Whatsapp', 'Twitter', 'Instagram','Tiktok'],
            datasets: [{
                label: 'Horas promedio / Dia',
                data: avg,
                backgroundColor: [
                    '#3b5998',  
                    '#075E54',
                    '#1DA1F2',
                    '#E1306C',
                    '#000000'
                ],
                maxBarThickness: 30,
                maxBarLength: 2
            }]
        },
        options: {
            legend: {
            display: false
         },
            scales: {
                yAxes:
                 [{
                    ticks: {
                        beginAtZero: true
                    }
                },
                {
                    scaleLabel: {
                      display: true,
                      labelString: 'Promedio de Horas/Dia'
                    }
                  }
            ],
                
            }
        }
    });
});


function send_with_ajax(url,params,callback){
    $.ajax({
        url: url,
        type: 'POST',
        data: params,
        dataType: 'json',
        contentType: false,
        processData: false,
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            callback(data);
            return false;
        }
        message_error(data.error);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus+': '+errorThrown);
    }).always(function (data) {

    });
}