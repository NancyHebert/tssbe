from config.settings import config

templates = {
	"account_verification": {
		"subject": "Thesis Supervisor Search verify email address | Vérification du votre boîte de réception",
		"plaintext": """
(English follows)

Bienvenue sur l'outil de recherche Trouver un directeur de thèse!

Votre code de vérification est : [verification_code]

Cliquer sur le lien suivant afin de compléter les informations nécessaires à créer votre profil : {front_end_address}?action=create-account&email=[email]&code=[verification_code]

Si vous n'êtes pas à l'origine de cette demande, vous pouvez ignorer ce message et le supprimer.

Veuillez ne pas répondre à ce courriel.
Si vous éprouvez des difficultés techniques, veuillez remplir le formulaire de demande d'assistance à http://www.med.uottawa.ca/medtech/help/fr.

Cordialement,

Le Bureau des études supérieures et postdoctorales
Faculté de médecine, Université d'Ottawa

----------------------------------------

Welcome to the Thesis Supervisor Search tool!

Your verification code is: [verification_code]

Please click the following link to continue creating your account: {front_end_address}?action=create-account&email=[email]&code=[verification_code]

If you received this email in error, you can safely ignore this email.

Please do not reply to this email.
If you experience technical difficulties, please submit an online help request at http://www.med.uottawa.ca/medtech/help/.

Kind Regards,

The Graduate and Postdoctoral Studies Office
Faculty of Medicine, University of Ottawa
			""".format(front_end_address = config["email"]["front_end_address"]),
		"html": """
			<html>
			<body>
			 <p><em>(English follows)</em></p>
			 <div>
			   <p>Bienvenue sur l'outil de recherche Trouver un directeur de thèse!</p>

			   <p>Votre code de vérification est : <b>[verification_code]</b></p>

			   <p>Cliquer sur le lien suivant afin de compléter les informations nécessaires à créer votre profil : <a href="{front_end_address}?action=create-account&email=[email]&code=[verification_code]">{front_end_address}?action=create-account&email=[email]&code=[verification_code]</a></p>

			   <p>Si vous n'êtes pas à l'origine de cette demande, vous pouvez ignorer ce message et le supprimer.</p>

			   <p>Veuillez ne pas répondre à ce courriel. <br>
			   Si vous éprouvez des difficultés techniques, veuillez remplir le <a href="http://www.med.uottawa.ca/medtech/help/fr">formulaire de demande d'assistance</a>.
			   </p>
			   <p>
				   Cordialement,
				   <br>
				   Le Bureau des études supérieures et postdoctorales <br>
				   Faculté de médecine, Université d'Ottawa

			   </p>
			 </div>
			 <hr>
			  <div>
			    <p>Welcome to the Thesis Supervisor Search tool!</p>

				<p>Your verification code is: <b>[verification_code]</b></p>

			    <p>Please click the following link to continue creating your account: <a href="{front_end_address}?action=create-account&email=[email]&code=[verification_code]">{front_end_address}?action=create-account&email=[email]&code=[verification_code]</a></p>

				<p>If you received this email in error, you can safely ignore this email.</p>

			    <p>Please do not reply to this email. <br>
				If you experience technical difficulties, please submit an <a href="http://www.med.uottawa.ca/medtech/help/">online help request</a>.
			    </p>
				<p>
			      Kind Regards,
			      <br>
			      The Graduate and Postdoctoral Studies Office<br>
				  Faculty of Medicine, University of Ottawa
		      	</p>
			  </div>
			</body>
			</html>
			""".format(front_end_address = config["email"]["front_end_address"])
	},
	"student_first_notification_to_researcher": {
		"subject": "[TSS] Message from student | Message d'un étudiant : [student_name]",
		"plaintext": """
(English follows)

----------------------------------------
Un message d'un étudiant suivera.
----------------------------------------

[message]

Profil de l'étudiant :
Nom : [student_name]
Statut d'admission : [admitted_fr]
Programme : [program_fr]
Niveau : [level_fr]
CV : [cvs_links]
Revelé(s) de notes : [transcripts_links]

Visionnez la conversation en ligne à {front_end_address}?conversationid=[token] pour répondre.

Vous n'êtes pas disponible pour superviser des étudiants? Vous pouvez modifier votre profil à {front_end_address} afin de mettre vos informations à jour.
Si vous éprouvez des difficultés techniques, veuillez remplir le formulaire de demande d'assistance à http://www.med.uottawa.ca/medtech/help/fr.

----------------------------------------
Message from student follows.
----------------------------------------

[message]

Student profile:
Name: [student_name]
Admitted status: [admitted_en]
Program: [program_en]
Level: [level_en]
CV: [cvs_links]
Transcripts: [transcripts_links]

View this conversation online at {front_end_address}?conversationid=[token] to reply.

If you are not available to take on graduate students, please update your profile information at {front_end_address}.
If you experience technical difficulties, please submit an online help request at http://www.med.uottawa.ca/medtech/help/.
		""".format(front_end_address = config["email"]["front_end_address"]),
		"html": """
			<html>
			<body>
		 	  <div>
			    <p><em>(English follows)</em></p>
			   	<!-- [missing_researcher_email] -->
			   	<hr>
			   	<p>Un message d'un étudiant suivera. <!-- Écrivez AU-DESSUS DE CETTE LIGNE pour répondre.</p>
			   	<p>Vos réponses seront visibles aux administrateurs de la Faculté de Médecine. --></p>
			   	<hr>
			   	<p>[message]</p>
			   	<p><b>Profil de l'étudiant :</b><br>
			   	<b>Nom :</b> [student_name]<br>
			   	<b>Statut d'admission :</b> [admitted_fr]<br>
			   	<b>Programme :</b> [program_fr]<br>
			   	<b>Niveau :</b> [level_fr] <br>
			   	<b>CV :</b> [cvs_links]<br>
			   	<b>Revelé(s) de notes :</b> [transcripts_links]</p>
			   	<hr>
			   	<p>Visionnez <a href="{front_end_address}?conversationid=[token]">la conversation en ligne</a> pour répondre.</p>
			   	<p>Vous n'êtes pas disponible pour superviser des étudiants? Vous pouvez <a href="{front_end_address}">modifier votre profil</a> afin de mettre vos informations à jour.</p>
			   	<p>Si vous éprouvez des difficultés techniques, veuillez remplir le <a href="http://www.med.uottawa.ca/medtech/help/fr">formulaire de demande d'assistance</a>.</p>
			  </div>
			  <hr>
			  <div>
			    <hr>
			    <p>Message from student follows. <!-- Write ABOVE THIS LINE to reply.</p>
			    <p>Replies will be visible to administrators in the Faculty of Medicine. --></p>
			    <hr>
			    <p>[message]</p>
			   	<p><b>Student profile:</b><br>
			   	<b>Name:</b> [student_name]<br>
			   	<b>Admitted status:</b> [admitted_en]<br>
			   	<b>Program:</b> [program_en]<br>
			   	<b>Level:</b> [level_en]<br>
			   	<b>CV:</b> [cvs_links]<br>
			   	<b>Transcripts:</b> [transcripts_links]</p>
			    <hr>
			   	<p>View <a href="{front_end_address}?conversationid=[token]">this conversation online</a> to reply.</p>
			    <p>If you are not available to take on graduate students, please <a href="{front_end_address}">update your profile information</a>.</p>
			    <p>If you experience technical difficulties, please submit an <a href="http://www.med.uottawa.ca/medtech/help/">online help request</a>.</p>
			  </div>
			</body>
			</html>
		""".format(front_end_address = config["email"]["front_end_address"])
	},
	"student_subsequent_notification_to_researcher": {
		"subject": "[TSS] Message from student | Message d'un étudiant : [student_name]",
		"plaintext": """
(English follows)

----------------------------------------
Un message d'un étudiant suivera.
----------------------------------------

[message]

----------------------------------------
Visionnez la conversation en ligne à {front_end_address}?conversationid=[token] pour répondre.
Si vous éprouvez des difficultés techniques, veuillez remplir le formulaire de demande d'assistance à http://www.med.uottawa.ca/medtech/help/fr.


----------------------------------------
Message from student follows.
----------------------------------------

[message]

----------------------------------------
View this conversation online at {front_end_address}?conversationid=[token] to reply.
If you experience technical difficulties, please submit an online help request at http://www.med.uottawa.ca/medtech/help/.
		""".format(front_end_address = config["email"]["front_end_address"]),
		"html": """
			<html>
			<body>
			<p><em>(English follows)</em></p>
			<div>
			  <hr>
			  <p>Un message d'un étudiant suivera. <!-- Écrivez AU-DESSUS DE CETTE LIGNE pour répondre.</p>
			  <p>Vos réponses seront visibles aux administrateurs de la Faculté de Médecine. --></p>
			  <hr>
			  <p>[message]</p>
			  <hr>
			  <p>Visionnez <a href="{front_end_address}?conversationid=[token]">la conversation en ligne</a> pour répondre.</p>
			  <p>Si vous éprouvez des difficultés techniques, veuillez remplir le <a href="http://www.med.uottawa.ca/medtech/help/fr">formulaire de demande d'assistance</a>.</p>
			</div>
			<hr>
			  <div>
			  	<!-- [missing_researcher_email] -->
			  	<br>
			    <hr>
			    <p>Message from student follows. <!--Write ABOVE THIS LINE to reply. </p>
			    <p>Replies will be visible to administrators in the Faculty of Medicine. --></p>
			    <hr>
			    <p>[message]</p>
			    <hr>

			    <p>View <a href="{front_end_address}?conversationid=[token]">this conversation online</a> to reply.</p>
			    <p>If you experience technical difficulties, please submit an <a href="http://www.med.uottawa.ca/medtech/help/" >online help request</a>.</p>
			  </div>
			</body>
			</html>
		""".format(front_end_address = config["email"]["front_end_address"])
	},
	"researcher_notification_to_student": {
		"subject": "[TSS] Message from researcher | Message d'un directeur de thèse : [researcher_name]",
		"plaintext": """
(English follows)

----------------------------------------
Un message d'un superviseur suivera.
----------------------------------------

[message]

Visionnez la conversation en ligne à {front_end_address}?conversationid=[token] pour répondre.
Si vous éprouvez des difficultés techniques, veuillez remplir le formulaire de demande d'assistance à http://www.med.uottawa.ca/medtech/help/fr.

----------------------------------------
Message from researcher follows.
----------------------------------------

[message]

View this conversation online at {front_end_address}?conversationid=[token] to reply.
If you experience technical difficulties, please submit an online help request at http://www.med.uottawa.ca/medtech/help/.
		""".format(front_end_address = config["email"]["front_end_address"]),
		"html": """
			<html>
			<body>
				<p><em>(English follows)</em></p>
				<div>
				  <hr>
				  <p>Un message d'un superviseur suivera. <!-- Écrivez AU-DESSUS DE CETTE LIGNE pour répondre.</p>
				  <p>Vos réponses seront visibles aux administrateurs de la Faculté de Médecine. --></p>
				  <hr>
				  <p>[message] </p>
				  <hr>
				  <p>Visionnez <a href="{front_end_address}?conversationid=[token]">la conversation en ligne</a> pour répondre.</p>
				  <p>Si vous éprouvez des difficultés techniques, veuillez remplir le <a href="http://www.med.uottawa.ca/medtech/help/fr">formulaire de demande d'assistance</a>.</p>
				</div>
				<hr>
			  <div>
			    <hr>
			    <p>Message from researcher follows. <!-- Write ABOVE THIS LINE to reply.</p>
			    <p>Replies will be visible to administrators in the Faculty of Medicine. --></p>
			    <hr>
			    <p>[message] </p>
				<hr>
			    <p>View <a href="{front_end_address}?conversationid=[token]">this conversation online</a> to reply.</p>
			    <p>If you experience technical difficulties, please submit an <a href="http://www.med.uottawa.ca/medtech/help/">online help request</a>.</p>
			  </div>

			</body>
			</html>
		""".format(front_end_address = config["email"]["front_end_address"])
	},
	"password_reset": {
		"subject": "[TSS] Password reset | Modification du votre mot de passe",
		"plaintext": """
(English follows)

Bienvenue à nouveau sur l'outil de recherche Trouver un directeur de thèse!

Nous avons reçu récemment une demande de modification du mot de passe pour votre compte.

Votre code de vérification : [verification_code]

Cliquer sur le lien suivant afin d'accéder à la page vous permettant de réinitialiser votre mot de passe : {front_end_address}?action=reset-password&email=[email]&code=[verification_code].

Vous devrez ensuite créer votre nouveau mot de passe et le confirmer.
Si vous ne souhaitez pas modifier votre mot de passe ou si vous n'êtes pas à l'origine de cette demande, vous pouvez ignorer ce message et le supprimer.
Si vous éprouvez des difficultés techniques, veuillez remplir le formulaire de demande d'assistance à http://www.med.uottawa.ca/medtech/help/fr.

Veuillez ne pas répondre à ce courriel.
Si vous avez des questions, communiquez avec nous à grad.med@uottawa.ca.

Cordialement,
Le Bureau des études supérieures et postdoctorales
Faculté de médecine, Université d'Ottawa

----------------------------------------

Welcome back to the Thesis Supervisor Search tool!
We recently received a request for a new password for this email.

Your verification code is: [verification_code]

Just follow this link to the password reset page: {front_end_address}?action=reset-password&email=[email]&code=[verification_code].
You will be asked to create a new password and confirm it.

If you received this email in error, you can safely ignore this email.
If you experience technical difficulties, please submit an online help request at http://www.med.uottawa.ca/medtech/help/.

Please do not reply to this email.
If you have questions please contact us at grad.med@uottawa.ca.

Kind Regards,

The Graduate and Postdoctoral Studies Office
Faculty of Medicine, University of Ottawa
		""".format(front_end_address = config["email"]["front_end_address"]),
		"html": """
			<html>
			<body>
			  <p><em>(English follows)</em></p>
			  <div>
			    <p>Bienvenue à nouveau sur l'outil de recherche Trouver un directeur de thèse! <br><br>
				Nous avons reçu récemment une demande de modification du mot de passe pour votre compte.</p>

			    <p>Votre code de vérification : <b>[verification_code]</b></p>

				<p>Cliquer sur le lien suivant afin d'accéder à la page vous permettant de <a href="{front_end_address}?action=reset-password&email=[email]&code=[verification_code]">réinitialiser votre mot de passe</a>.</p>
 				<p>Vous devrez ensuite créer votre nouveau mot de passe et le confirmer.</p>
				<p>Si vous ne souhaitez pas modifier votre mot de passe ou si vous n'êtes pas à l'origine de cette demande, vous pouvez ignorer ce message et le supprimer.<br>
				 Si vous éprouvez des difficultés techniques, veuillez remplir le <a href="http://www.med.uottawa.ca/medtech/help/fr">formulaire de demande d'assistance</a></p>

			    <p>Veuillez ne pas répondre à ce courriel.</p>
				<p>Si vous avez des questions, communiquez avec nous à <a href="mailto:grad.med@uottawa.ca">grad.med@uottawa.ca</a></p>

				<p>
			      <br>
			      Cordialement,
			      <br>
			      Le Bureau des études supérieures et postdoctorales<br>
				  Faculté de médecine, Université d'Ottawa
				  </p>
			  </div>
			  <hr>
			  <div>
			    <p>Welcome back to the Thesis Supervisor Search tool! <br><br>
				We recently received a request for a new password for this email.</p>

			    <p>Your verification code is: <b>[verification_code]</b></p>

				<p>Just follow this link to the password reset page: <a href="{front_end_address}?action=reset-password&email=[email]&code=[verification_code]">Reset my password</a>.</p>
				<p>You will be asked to create a new password and confirm it.</p>

				<p>If you received this email in error, you can safely ignore this email.</p>
				<p>If you experience technical difficulties, please submit an <a href="http://www.med.uottawa.ca/medtech/help/">online help request</a>.</p>

			    <p>Please do not reply to this email. <br>
				<p>If you have questions please contact us at <a href="mailto:grad.med@uottawa.ca">grad.med@uottawa.ca</a></p>
			      Kind Regards,
			      <br>
			      The Graduate and Postdoctoral Studies Office<br>
				  Faculty of Medicine, University of Ottawa

				</p>
			  </div>
			</body>
			</html>
		""".format(front_end_address = config["email"]["front_end_address"])
	},
}
