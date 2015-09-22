$(function () {
    /**
     * Side menu nav
     */
    var nav_dropdown_toggle = $('.nav-side-menu a.dropdown-toggle');
    nav_dropdown_toggle.on('click', function (e) {
        e.preventDefault();
        var parent_li = $(this).parents('li'),
            dropdown = $('ul.dropdown', parent_li);
        parent_li.toggleClass('open');
        if (!dropdown.is(':visible')) {
            dropdown.slideUp();
        } else {
            dropdown.slideDown();
        }

    });

    /**
     * Scroller for nav menu
     */

    $('.nav-side-menu-content').baron();

    /**
     * Sticky buttons
     */
    $(".grid-controls").sticky({topSpacing:45});
});