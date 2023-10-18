/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.MyCarousel = publicWidget.Widget.extend({
    selector: '.s_snippet_carousel',

    /**
     * @override
     */
    init() {
        tns({
            mode: 'carousel', // or 'gallery'
            mouseDrag: true,
            navPosition: "bottom",
            gutter: 10,
            controlsContainer: "#custom_controlsContainer",
            nextButton: '#prev',
            nextButton: '#next', // String selector
            arrowKeys: true, // keyboard support
            lazyload: false,
            lazyloadSelector: ".tns-lazy",
            responsive: {
              "350": {
                "items": 1,
                "controls": true,
                "edgePadding": 30
              },
              "500": {
                "items": 3
              }
            },
          });
    }
});

export default publicWidget.registry.MyCarousel;
