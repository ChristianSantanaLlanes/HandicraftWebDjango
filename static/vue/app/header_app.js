new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: {
        lista_secciones: [],
        lista_categorias: []
    },
    methods: {
        getSecciones: function () {
            self = this
            axios.get('/api/v1/secciones/')
            .then((response => {
                self.lista_secciones = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created () {
        this.getSecciones();
    },
})