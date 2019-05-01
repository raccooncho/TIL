function makeArticle (id, title, content) {
    return {
        id: id,
        title: title,
        content: content,
        makeOne: function () {
            return `${this.id} 번 글: ${this.title} > ${this.content}`
        }
    }
}

function makeArticle (id, title, content) {
    return {
        id, title, content,
        makeOne () {
            return `${this.id} 번 글: ${this.title} > ${this.content}`
        }
    }
}