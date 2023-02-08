import view
import model

def start():
    user_chioce = 0
    while user_chioce!=8:
        user_chioce = view.main_menu()

        match user_chioce:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                change = view.change_contact()
                answer = model.change_phone_book(change)
                view.changeable_contact(answer)
                new_contakt = list(view.new_contact())
                model.change_contact_phone_book(new_contakt)
                view.result_change()
            case 6:
                delete_search = view.del_contact()
                delete = model.delete_contact(delete_search)
                view.result_del()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)

