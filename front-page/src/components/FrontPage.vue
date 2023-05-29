<template>
<div style="display: flex; justify-content: space-between; padding: 1rem; background-color: #212A3E; color: white; align-items: center">
    <h1 class="title">Front Page</h1>
    <div style="display: flex; align-items: center">
    <div class="sort-bar">
      <label style="padding-right: 0.5rem" for="sort-select">Sort By:</label>
      <select class="btn btn-secondary" id="sort-select" v-model="sortBy" @change="sortPosts">
        <option class="dropdown-item" value="title">Title</option>
        <option class="dropdown-item" value="author">Author</option>
        <option class="dropdown-item" value="score">Score</option>
      </select>
    </div>
      <button class="btn btn-sm btn-secondary" @click="toggleSortDirection">
        {{ sortDirection === 'asc' ? 'Sort Descending' : 'Sort Ascending' }}
      </button>
    </div>
    </div>
  <div class="front-page">
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else>
	<div class="row" style="justify-content:center">
       <div v-for="post in sortedPosts" :key="post.id" class="card post-card col-lg-6 col-md-12 col-sm-12">
        <div class="card-body" style="display: flex; justify-content:space-between; flex-direction:column">
        <div>
        <div>
          <h3 class="card-title">{{ post.title }}</h3>
          <h4 class="card-subtitle mb-2 text-muted">{{ "r/" + post.subreddit }}</h4>
          <hr/>
        </div>
          <p class="card-text">{{ post.body }}</p>
        </div>
          <div>
          <hr/>
          <div style="display: flex; justify-content: space-between">
             <div style="display: flex; align-items: center">
                <p class="author" style="padding-right: 1rem"> u/{{ post.author }}</p>
                <p v-if="post.author_flair_text !== null" class="author-flair">{{ post.author_flair_text }}</p>
             </div>
             <p class="card-text">Upvotes: {{ post.score }}</p>
          </div>
          </div>
        </div>
     </div>
    </div>
	</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: [],
      loading: true,
      sortBy: 'title',
      sortDirection: 'asc',
    };
  },
  computed: {
    sortedPosts() {
		const direction = this.sortDirection === "asc" ? 1 : -1;
      let sorted = [...this.posts];
      sorted.sort((a, b) => {
        if (a[this.sortBy] < b[this.sortBy]) return -1 * direction;
        if (a[this.sortBy] > b[this.sortBy]) return 1 * direction;
        return 0;
      });
      return sorted;
    },
  },
  mounted() {
    // Make an API call to retrieve the posts
    fetch('http://127.0.0.1:8000/api/data/')
      .then(response => response.json())
      .then(data => {
        this.posts = data.map(post => {
			return {
				...post,
				title: post.permalink.split("/")[5].split("_").map(x => x.charAt(0).toUpperCase() + x.substring(1)).join(" "),
			};
		});
        this.loading = false;
      })
      .catch(error => {
        console.error('Error:', error);
        this.loading = false;
      });
  },
  methods: {
    sortPosts() {
      this.posts = this.sortedPosts;
    },
	toggleSortDirection() {
    this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
	},
  },
};
</script>

<style scoped>
.front-page {
  margin: 0 auto;
  padding: 20px;
  background-color: #F1F6F9;
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.sort-bar {
  padding-right: 10px;
}

.loading {
  font-size: 18px;
  text-align: center;
  margin-top: 50px;
}

.post-card {
  background-color: #FFFFFF;
  max-width: 800px;
  margin: 10px;
}

.author-flair {
  font-size: 14px;
  color: #666;
  margin-bottom: 0;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.card-subtitle {
  font-size: 16px;
  margin-bottom: 10px;
  color: #666;
}

.card-text {
  font-size: 16px;
  margin-bottom: 10px;
}

.card-text:last-child {
  margin-bottom: 0;
}

.author {
  font-size: 16px;
  margin-bottom: 0;
}

.dropdown-item {
  color: black;
  background-color: white;
}

</style>
