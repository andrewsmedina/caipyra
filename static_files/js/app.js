(function() {
    var btn = document.querySelector('.btn-default'),
        form = document.querySelector('.form-dreams');

    function fadeIn(el) {
        el.style.opacity = 0;
        el.style.display = 'block';

        var last = +new Date();
        var tick = function() {
            el.style.opacity = +el.style.opacity + (new Date() - last) / 400;
            last = +new Date();

            if (+el.style.opacity < 1) {
                (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
            }
        };

        tick();
    }

    function fadeOut(el, fn) {
        el.style.opacity = 1;

        var last = +new Date();
        var tick = function() {
            el.style.opacity = el.style.opacity - (new Date() - last) / 400;
            last = +new Date();

            if (+el.style.opacity > 0) {
                el.style.display = 'none';
                (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
                fn();
            }
        };

        tick();
    }

    btn.addEventListener('click', function(e) {
        fadeOut(btn, function() {
            fadeIn(form);
        });
    });

})();