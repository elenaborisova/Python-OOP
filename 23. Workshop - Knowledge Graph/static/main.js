function drawGraph(term) {
    anychart.data.loadJsonFile(`/api/build-graph?term=${term}`, function (data) {
        console.log(data);
        var graph = anychart.graph(data);
        graph.container('contents').draw();
        graph.nodes().labels().enabled(true);
        graph.nodes().labels().format("{%id}");
    });
}


document.getElementById('search-form').onsubmit = function(event) {
    event.preventDefault();
    const term = event.target.term.value;
    drawGraph(term);
}
