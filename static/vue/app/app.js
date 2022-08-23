new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: {
        lista: [],
        lista_secciones: [],
        lista_categorias: [],
        lista_blog: [],
        elemento1: {},
        elemento2: {},
        elemento3: {}
    },
    methods: {
        getASimple: function () {
            this.elemento1 = this.lista_blog[0]
            this.elemento2 = this.lista_blog[1]
            this.elemento3 = this.lista_blog[2]
        },
        getBlog: function () {
            self = this;
            axios.get('/api/v1/blogs/')
            .then((response) => {
                self.lista_blog = response.data
                this.getASimple()
            })
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created () {
        this.getBlog();
    },
})