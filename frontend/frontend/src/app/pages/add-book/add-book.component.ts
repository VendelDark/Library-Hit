import { Component } from '@angular/core';
import { BookService } from '../../services/book.service';
import { Book } from '../../models/book.model';

@Component({
  selector: 'app-add-book',
  templateUrl: './add-book.component.html'
})
export class AddBookComponent {
  book: Book = {
    title: '',
    author: '',
    year: new Date().getFullYear(),
    genre: '',
    synopsis: ''
  };

  constructor(private bookService: BookService) {}

  addBook() {
    this.bookService.addBook(this.book).subscribe((newBook) => {
      console.log('Livro adicionado:', newBook);
      // Lógica adicional para sucesso
    });
  }
}
