<!-- eslint-disable vue/no-parsing-error -->

<script setup lang="ts">
import { ref } from 'vue'

const filer = ref(null)

const up = async () => {
  const formData = new FormData()
  formData.append('name', 'file')
  formData.append('file', filer.value)
  const res = await fetch('http://localhost:8000/filer/', {
    method: 'POST',
    body: formData
  })
  console.log(await res.json())
}
</script>

<template>
  <main>
    <div>
      {{ filer }}
      <input type="file" @change="(e) => {filer = e.target.files[0]}">

      <button @click="up()">
        Send
      </button>

    </div>
  </main>
</template>
