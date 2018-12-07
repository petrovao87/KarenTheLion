from db_lion import db_session, AnswersLion, AnswersAnother, User
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import datetime
import API_file
import random


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def callback_alarm(bot, job):

    rand_alarm = random.randint(1,10)
    alarm = db_session.query(AnswersLion).filter(AnswersLion.id==rand_alarm).all()
    print(alarm)
    for content in alarm:

        content_msg = content.__dict__['content']
        bot.send_message(chat_id=job.context, text=content_msg)






def callback_timer(bot, update, job_queue):
    print("start")
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    #lion_chat = update.effective_user.chat
    print(user_id)
    print(user_name)


    if user_id == 192967689:

        bot.send_message(chat_id=update.message.chat_id,
                    text='Игра начинается')
    
        #job_repeat = job_queue.run_repeating(callback_alarm, interval=10, context=update.message.chat_id)
        job_repeat = job_queue.run_daily(callback_alarm, time=datetime.time(7, 30, 00), context=update.message.chat_id)
        print("111")

    elif user_id == 244744683:
        bot.send_message(chat_id=update.message.chat_id,
                    text = ("""
Каренчик ван лав

____s$$$ssss$$s______sssss$$$s 
___$$s§§§§§§§§§s$__$s§§§§§§§§§$$ 
___³§§§§§§§§§§§§§s_s§§§§§§§§§§§§§³ 
___§§§§§§§§§§§§§§§s§§§§§§§§§§§§§§ 
___³§§§§§§§§§§§§§§§§§§§§§§§§§§§§§ 
____³§§§§§§§§§§§§§§§§§§§§§§§§§§§³ 
_____³§§§§§§§§§§§§§§§§§§§§§§§§§³ 
______³§§§§§§§§§§§§§§§§§§§§§§§³ 
________³§§§§§§§§§§§§§§§§§§§³ 
__________³§§§§§§§§§§§§§§§³ 
____________³§§§§§§§§§§§³ 
_______________³§§§§§³ 
_________________³§³ 
 """))

    else:
        bot.send_message(chat_id=update.message.chat_id,
                    text = ("{}, ах ты шелудивый пёс! Иди гусей еби".format(user_name)))



def chat_bot(bot, update):
    #time = datetime.time.today()
    print("chat")

    lion_id = update.effective_user.id
    print(lion_id)

    rand_answers = random.randint(1,10)
    rand_answers_lion = random.randint(11,15)
    #answers = db_session.query(AnswersAnother).filter(AnswersAnother.id==rand_answers).all()

    #print(answers)
    #for answrs in answers:

       # answers_id = answrs.__dict__['content']

    if lion_id == 1192967689:

        bot.send_message(chat_id=update.message.chat_id,
                    text="""Великий господин, мудрейший и светлейший! 
Подчиняюсь тебе.
Хруст пидор.""")

    elif lion_id == 192967689:
        answers = db_session.query(AnswersAnother).filter(AnswersAnother.id==rand_answers_lion).all()
        for answrs in answers:

            answers_id = answrs.__dict__['content']
            bot.send_message(chat_id=update.message.chat_id,
                    text = "{}".format(answers_id)) 


    else:
        answers = db_session.query(AnswersAnother).filter(AnswersAnother.id==rand_answers).all()
        for answrs in answers:

            answers_id = answrs.__dict__['content']
            bot.send_message(chat_id=update.message.chat_id,
                    text = "{}".format(answers_id))    


def job_stop(bot, update, job_queue):
    print("stop")
    #job_repeat = job_queue.run_repeating(callback_alarm, interval=50, context=update.message.chat_id)
    #j.stop()
    #callback_alarm.schedule_removal() 
    #callback_timer.schedule_removal()
    #job_queue.schedule_removal()


def main():
    updtr = Updater(API_file.TELEGRAM_API_KEY)
    updtr.dispatcher.add_handler(CommandHandler("chat", chat_bot))
    timer_handler = CommandHandler('game', callback_timer, pass_job_queue=True)
    timer_handler2 = CommandHandler('stop', job_stop, pass_job_queue=True)
    updtr.dispatcher.add_handler(timer_handler)
    #updtr.dispatcher.add_handler(timer_handler2)
    #updtr.dispatcher.add_handler(CommandHandler("stop", job_stop, pass_job_queue=True))
    #updtr.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))
    j = updtr.job_queue
    updtr.start_polling()
    updtr.idle()



if __name__ == "__main__":
    logging.info("bot started")
    #data = get_bit("https://api.coinmarketcap.com/v1/ticker/")
    print("start huyart")
    #time1 = datetime.today()
    #print(time1)
    time2 = datetime.datetime.now()
    print(time2)
    main()
    #send_message()