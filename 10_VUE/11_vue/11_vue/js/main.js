// json-server 의 기본 접속 URI 는 아래와 같습니다. 필요에 따라 수정 가능합니다.
const HOST = "http://localhost:3000";

const app = new Vue({
    el: "#app",
    data: {
        logo: 'MO<i class="fab fa-vuejs"></i>IE',
        isMain: true,
        genres: [],
        movies: [  // 현재 하드 타이핑 된 배열이지만, 실제로는 axios.get() 을 통해 API server 로 부터 받아옵니다.
        ],
        search: '', // 검색 기능을 구현할 때, 사용자의 입력 값을 이곳에 쌍방향 바인딩 합니다.

        isDetail: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
        movieDetail: {},  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
        inputScore: {
            content: "",
            score: 0,
            movieId: null,
        },
        scores: {},
        asc: true,
    },
    methods: {
        async toggleDetail(id = null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
            if (id) {
                // const res = await axios.get(`${HOST}/movies/${id}`);
                // this.movieDetail = res.data;
                this.movieDetail = this.movies.find(movie => movie.id === id);

                const res = await axios.get(`${HOST}/movies/${id}/scores`);
                this.scores = res.data;
            }

            this.isDetail = !this.isDetail
        },
        async getMovies(genreId = null) {
            const URL = genreId ? `${HOST}/genres/${genreId}/movies` : `${HOST}/movies`;
            const res = await axios.get(URL);
            this.movies = res.data;
        },
        async postScore(movieId) {

            function getAverageScore(scores) {
                const result = scores.reduce((acc, score) => {
                    acc.total += score.score;
                    acc.cnt++;
                    return acc
                }, {total: 0, cnt: 0});
                if (result.cnt) {
                    return (result.total / result.cnt).toFixed(2);
                } else {
                    return 0;
                }

            }

            if (movieId && this.inputScore.content) {
                this.inputScore.movieId = movieId;
                const response = await axios.post(`${HOST}/scores`, this.inputScore);
                const newScore = response.data;
                console.log(this.inputScore);
                this.scores.push(newScore);
                this.inputScore.score = 0;
                this.inputScore.content = "";
                const res = await axios.patch(`${HOST}/movies/${movieId}`, {averageScore: getAverageScore(this.scores)})
                this.movieDetail = res.data;
            } else {
                alert('리뷰를 입력하세요!!!')
            }
        },
        orderMovies (standard='', asc = this.asc) {
            this.movies = this.movies.sort(function(a, b) {
                if (asc) {
                    return Number(b[standard]) - Number(a[standard]);
                } else {
                    return Number(a[standard]) - Number(b[standard]);
                }
            });
            console.log(this.asc, this.movies);
            this.asc = !this.asc;
        }
    },
    computed: {

    },

    watch: {
        async search(keyword) {
            const res = await axios.get(`${HOST}/movies?title_like=${keyword}&description_like=${keyword}`);
            this.movies = res.data
        },
        async movies() {
            this.isDetail = false;
        }
    },
    /*
    Vue Instance LIFE CYCLE
     */
    created: function () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, json-server 에서 장르목록만 받아옵니다.
        axios.get(`${HOST}/genres`)  // 만약 json-server 를 사용하지 않거나 서버가 꺼져있다면 에러가 발생합니다.
            .then(res => this.genres = res.data);
        axios.get(`${HOST}/movies`)
            .then(res => this.movies = res.data);
    },
});

document.addEventListener('keyup', e => {
    if (e.key === 'Escape') {
        app.$data.isDetail = false;
    }
});