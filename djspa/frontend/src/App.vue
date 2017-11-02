<template>
    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <h1>Http</h1>
                <div class="form-group">
                    <label>Username</label>
                    <input type="text" class="form-control" v-model="user.username">
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="text" class="form-control" v-model="user.email">
                </div>
                <div class="btn btn-primary" @click="submit">Submit</div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                user: {
                    username: '',
                    email: ''
                }
            }
        },
        methods: {
            submit() {
                console.log(this.user);
                this.$http.get('http://localhost:8000/api/?format=json').then(
                    response => {
                        console.log(response)
                    }, error => {
                        console.log(error)
                    }
                )

            }
        }
    }
</script>

<style>
</style>