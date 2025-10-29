<template>
    <footer style="background-color: var(--black); color: #fff;">
        <div class="flex-row alitems-center justy-center small-padding" style="height: 60px; background-color: var(--deep-dark);">
            <div class="flex-row alitems-center container-width mobile-wrap-column " style="justify-content: space-between;">
                <img :src="LogoImg"  />
                <img :src="CopyrightImg" style="width: calc(35% + 100px); max-width: 400px;" />
            </div>
        </div>
    </footer>
</template>
<script setup>
import CopyrightImg from '@/assets/copyright.svg'
import LogoImg from '@/assets/logo.svg'
</script>