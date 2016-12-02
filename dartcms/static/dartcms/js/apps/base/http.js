var request = {
    'GET': {}
};

decodeURI(location.search).substr(1).split("&").forEach(function (item) {
    request.GET[item.split("=")[0]] = item.split("=")[1].replace(/\+/g, ' ');
});