// json-server 의 기본 접속 URI 는 아래와 같습니다. 필요에 따라 수정 가능합니다.
const HOST = "http://localhost:3000";

const app = new Vue({
  el: "#app",
  data: {
    header: 'MO<i class="fab fa-vuejs"></i>IE',
    genres: [],
    movies: [],
    scores: [],
    search: '',
  },
  methods: {
    getMovies () {

    }
  },
  computed: {},
  watch: {
    search (keyword) {
      axios.get(`${HOST}/movies?q=${keyword}`)
        .then(res => this.movies = res.data)
    }
  },
});