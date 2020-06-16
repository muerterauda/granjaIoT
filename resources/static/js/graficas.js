google.charts.load('current', {'packages': ['gauge', 'corechart']});
google.charts.setOnLoadCallback(drawChart);
var options_comida = {
    colors: ["#088A08"],
    series: [parseInt($('#comida-value').val(), 10)],
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
    labels: ['Comida restante'],
};
var options_agua = {
    colors: ["#0000FF"],
    series: [parseInt($('#agua-value').val(), 10)],
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
    labels: ['Agua restante'],
};
var chart_agua = new ApexCharts(document.querySelector("#chart_agua"), options_agua);
chart_agua.render();
var chart_comida = new ApexCharts(document.querySelector("#chart_comida"), options_comida);
chart_comida.render();

function drawChart() {

    let dataTemperatura = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Temperatura', parseInt($('#temperatura-value').val(), 10)]
    ]);
    let dataHumedad = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Humedad', parseInt($('#humedad-value').val(), 10)]
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
            let data_1 = [['Fecha', 'Temperatura', 'Humedad']], data_2 = [['Fecha', 'Tanque', 'Silo']],
                data_3 = [['Fecha', 'Bebedero', 'Comedero']];
            let i = res.length - 1;
            for (i; i >= 0; i--) {
                let m = res[i];
                data_1.push([m.fecha, m.temperatura, m.humedad]);
                data_2.push([m.fecha, m.agua, m.humedad]);
            }

            let options_1_t = {
                legend: {position: 'bottom', textStyle: {fontSize: 16}},
                height: 300,
                colors: ['red', 'blue']
            };
            let options_2_t = {
                legend: {position: 'bottom', textStyle: {fontSize: 16}},
                height: 300,
                colors: ['blue', 'red']
            };
            let options_3_t = {
                title: 'Estado del comedero y del bebedero',
                legend: {position: 'bottom'}
            };

            let chart_1_t = new google.visualization.LineChart(document.getElementById('chart_div_temp_hum_t'));
            let chart_2_t = new google.visualization.LineChart(document.getElementById('chart_div2_tanque_silo_t'));

            chart_1_t.draw(google.visualization.arrayToDataTable(data_1), options_1_t);
            chart_2_t.draw(google.visualization.arrayToDataTable(data_2), options_2_t);
        },
        error: function (res) {
            alert("Error en la conexión con el servidor.");
        }
    });
}