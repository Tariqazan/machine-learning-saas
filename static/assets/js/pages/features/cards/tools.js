"use strict";

var KTCardTools = function () {
    // Toastr
    var initToastr = function() {
        toastr.options.showDuration = 1000;
    }

    // Demo 1
    var demo1 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_1');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }
    // Demo 1
    var demo2 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_2');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo3 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_3');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {
            toastr.info('Leload event fired!');

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }
    // Demo 1
    var demo4 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_4');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo5 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_5');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo6 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_6');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo7 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_7');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo8 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_8');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo9 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_9');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo10 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_10');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    // Demo 1
    var demo11 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_11');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }

    var demo12 = function() {
        // This card is lazy initialized using data-card="true" attribute. You can access to the card object as shown below and override its behavior
        var card = new KTCard('kt_card_12');

        // Toggle event handlers
        card.on('beforeCollapse', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterCollapse', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        card.on('beforeExpand', function(card) {
            setTimeout(function() {
            }, 100);
        });

        card.on('afterExpand', function(card) {
            setTimeout(function() {
            }, 2000);
        });

        // Reload event handlers
        card.on('reload', function(card) {

            KTApp.block(card.getSelf(), {
                overlayColor: '#ffffff',
                type: 'loader',
                state: 'primary',
                opacity: 0.3,
                size: 'lg'
            });

            // update the content here

            setTimeout(function() {
                KTApp.unblock(card.getSelf());
            }, 2000);
        });
    }


    return {
        //main function to initiate the module
        init: function () {
            initToastr();

            // init demos
            demo1();
            demo2();
            demo3();
            demo4();
            demo5();
            demo6();
            demo7();
            demo8();
            demo9();
            demo10();
            demo11();
            demo12();
        }
    };
}();

jQuery(document).ready(function() {
    KTCardTools.init();
});