from django.shortcuts import HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.shortcuts import render
from .forms import PostForm
# Post modelini import edelim
from .models import Post
# Kullanıcıya yaptığı işlemleri mesaj olarak göstermesi için
from django.contrib import messages



# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    #posts adında bir değişken tanımlıyorum
    # HttpResponse methodunu render ile değiştireceğiz
    # render fonksiyonu kullanmak için bir html dosyamız olmalı
    # template klasörü altında post adında yeni bir klasör oluşturduk.
    # post ile ilgli bütün html dosyalarını bu klasörün altında toplayalım.
    # bunun için klasörün içinde index.html adında dosya oluşturuyorum
    # bu html dosyasının içi şimdilik boş kalsın ve render fonskisyonu içine adresini verelim.
    # post listesini içerik olarak göndereceğiz
    # tırnak içinde yazılan posts templatte kullanılacak olan
    # diğer posts ise bizim veritabanından getireceğimiz listeyi tutan bir değişken
    # şimdi template dönelim ve index.html dosyasına geçiyorum
    # buradaki her postu ekrana yazdırmak için for döngüsüne ihtiyacım olacak.
    # hmtl dosyalarında for, if gibi ifadeleri kullanmak için {% %} kullanmalısın
    return render(request,'post/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id) # id=2 olan postu getirmesini istiyoruz.
    context = {
        'post': post,
    }
    return render(request,'post/detail.html', context)

def post_create(request):

    # if request.method == "POST":
    #   print(request.POST)

    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Post.objects.create(title=title, content=content)

    #  if request.method == "POST":
    #     # save info which came from form
    #     form = PostForm(request.POST)
    #     if form.is_valid(): # bu fonksiyon ile formun doğru doldurup doldurulmadığını kontrol ediyoruz.
    #         form.save()
    # else:
    #     # show the form to user
    #     form = PostForm()

    form = PostForm(request.POST or None) # bunun anlamı şudur dolu gelirse para metre al boş gelirse hiç parametre alma
    # bu sayede her iki senaryoya uyacak şekilde dinamik hale getirdik.
    # yukarıdakilerden alternatif olarak bunu kullanabilirsin
    if form.is_valid():
        post = form.save()
        messages.success(request, 'you have successfully created a post')
        return HttpResponseRedirect(post.get_absoulute_url())

    context = {
        'form': form,
    }

    return render(request,'post/form.html', context)



def post_update(request, id):
    post = get_object_or_404(Post, id=id) # post getirme kodu
    form=PostForm(request.POST or None, instance= post)   # form getime kodu
    if form.is_valid():    #formdan gelenleri doğrulayıp kaydetmek için
        form.save()
        messages.success(request, 'you have successfully updated a post', extra_tags='post-success')
        # burada post nesnesini getirmeye gerek yok çünkü 2 satır yukarıda post nesnesini getirmiştik.
        return HttpResponseRedirect(post.get_absoulute_url())
    context = {       
        'form': form, 
    }                 
    return render(request, 'post/form.html', context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')