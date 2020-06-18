google.charts.load('current', {'packages': ['gauge', 'corechart']});
google.charts.setOnLoadCallback(drawChart);
var options_silo_tanque = {
    colors: ["#088B00", "#0000FF"],
    series: [parseInt($('#comida-value').val(), 10), parseInt($('#agua-value').val(), 10)],
    chart: {
        height: 250,
        type: 'radialBar',
    },
    plotOptions: {
        radialBar: {
            hollow: {
                size: '50%',
            }
        },
    },
    labels: ['Comida restante', 'Agua restante'],
};
var options_comedero_bebedero = {
    colors: ["#2bba0b", "#00AAFF"],
    series: [parseInt($('#comedero-value').val(), 10), parseInt($('#bebedero-value').val(), 10)],
    chart: {
        height: 250,
        type: 'radialBar',
    },
    plotOptions: {
        radialBar: {
            hollow: {
                size: '50%',
            }
        },
    },
    labels: ['Comida restante', 'Agua restante']
};
var chart_conjunto_1 = new ApexCharts(document.querySelector("#chart_conjunto_1"), options_silo_tanque);
chart_conjunto_1.render();
var chart_conjunto_2 = new ApexCharts(document.querySelector("#chart_conjunto_2"), options_comedero_bebedero);
chart_conjunto_2.render();

function drawChart() {

    let dataTemperatura = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['', parseInt($('#temperatura-value').val(), 10)]
    ]);
    let dataHumedad = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['', parseInt($('#humedad-value').val(), 10)]
    ]);

    let optionsTemperatura = {
        min: -20, max: 60,
        width: 400, height: 200,
        redFrom: 50, redTo: 100,
        yellowFrom: 30, yellowTo: 50,
        minorTicks: 5
    };

    let optionsHumedad = {
        min: 0, max: 100,
        width: 400, height: 200,
        redFrom: 90, redTo: 100,
        yellowFrom: 60, yellowTo: 90,
        minorTicks: 5
    };

    let chart = new google.visualization.Gauge(document.getElementById('chart_div_temp'));
    let chart2 = new google.visualization.Gauge(document.getElementById('chart_div2_hum'));

    chart.draw(dataTemperatura, optionsTemperatura);
    chart2.draw(dataHumedad, optionsHumedad);

    $.ajax({
        url: "/granjaIoT/get_ultimas_mediciones",
        type: 'GET',
        data: {
            cantidad: 10
        },
        success: function (res) {
            res = JSON.parse(res);
            let data_1 = [['Fecha', 'Temperatura']], data_2 = [['Fecha', 'Humedad']],
                data_3 = [['Fecha', 'Silo', 'Tanque']], data_4 = [['Fecha', 'Comedero', 'Bebedero']];
            let i = res.length - 1;
            for (i; i >= 0; i--) {
                let m = res[i];
                data_1.push([m.fecha, m.temperatura]);
                data_2.push([m.fecha, m.humedad]);
                data_3.push([m.fecha, m.comida, m.agua]);
                data_4.push([m.fecha, m.comedero, m.bebedero]);
            }

            let options_temp = {
                legend: {position: 'bottom', textStyle: {fontSize: 16}},
                vAxis: { ticks: [-30,-20,-10,0,10,20,30,40,50,60,70] },
                lineWidth: 7,
                hAxis: {textStyle: {fontSize: 12}},
                chartArea: {width: '85%', height: '75%'},
                height: 550,
                colors: ['red']
            };

            let options_hum = {
                legend: {position: 'bottom', textStyle: {fontSize: 16}},
                vAxis: { ticks: [0,10,20,30,40,50,60,70,80,90,100] },
                lineWidth: 7,
                hAxis: {textStyle: {fontSize: 12}},
                chartArea: {width: '85%', height: '75%'},
                height: 550,
                colors: ['blue']
            };
            let options_silo_tanque = {
                legend: {position: 'bottom', textStyle: {fontSize: 16}},
                vAxis: { ticks: [0,10,20,30,40,50,60,70,80,90,100] },
                lineWidth: 7,
                hAxis: {textStyle: {fontSize: 12}},
                chartArea: {width: '85%', height: '75%'},
                height: 550,
                colors: ["#088B00", "#0000FF"]
            };
            let options_comedero_bebedero = {
                legend: {position: 'bottom', textStyle: {fontSize: 16}},
                vAxis: { ticks: [0,10,20,30,40,50,60,70,80,90,100] },
                lineWidth: 7,
                hAxis: {textStyle: {fontSize: 12}},
                chartArea: {width: '85%', height: '75%'},
                height: 550,
                colors: ["#2bba0b", "#00AAFF"]
            };

            let chart_1_t = new google.visualization.LineChart(document.getElementById('chart_div_temp_t'));
            let chart_2_t = new google.visualization.LineChart(document.getElementById('chart_div_hum_t'));
            let chart_3_t = new google.visualization.LineChart(document.getElementById('chart_div_silo_tanque_t'));
            let chart_4_t = new google.visualization.LineChart(document.getElementById('chart_div_com_beb_t'));

            chart_1_t.draw(google.visualization.arrayToDataTable(data_1), options_temp);
            chart_2_t.draw(google.visualization.arrayToDataTable(data_2), options_hum);
            chart_3_t.draw(google.visualization.arrayToDataTable(data_3), options_silo_tanque);
            chart_4_t.draw(google.visualization.arrayToDataTable(data_4), options_comedero_bebedero);
        },
        error: function (res) {
            alert("Error en la conexión con el servidor.");
        }
    });
}