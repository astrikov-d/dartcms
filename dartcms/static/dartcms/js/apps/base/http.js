var request = {
    'GET': {}
};

location.search.substr(1).split("&").forEach(function (item) {
    request.GET[item.split("=")[0]] = item.split("=")[1]
});