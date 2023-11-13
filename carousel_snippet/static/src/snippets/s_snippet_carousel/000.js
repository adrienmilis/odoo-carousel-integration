/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.MyCarousel = publicWidget.Widget.extend({
    selector: '.s_snippet_carousel',

    /**
     * @override
     */
    init() {
        this._super.apply(this, arguments);
        // Initialize the slider (see github doc)
        let sliders = document.querySelectorAll('.slider');
        for (let i = 0; i < sliders.length ; ++i) {
            tns({
                container: sliders[i],
                mode: 'carousel', // or 'gallery'
                mouseDrag: true,
                nav: false,
                gutter: 10,
                controlsContainer: ".custom_controlsContainer",
                nextButton: '.prev',
                nextButton: '.next', // String selector
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
    }
});

export default publicWidget.registry.MyCarousel;
